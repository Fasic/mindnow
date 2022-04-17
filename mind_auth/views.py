from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, AllowAny

from rest_api.serializers import UserSerializer, RegisterSerializer
from travelling_companion.forms import RegistrationForm, PersonForm, PassportForm

""" Auth views, WEB and API """


class UserList(generics.ListCreateAPIView):
    """ Api view for listing all users, permission required: IsAdminUser. """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]


class RegisterView(generics.CreateAPIView):
    """ Api view for registration, permission required: None. """
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class RegistrationView(View):
    """ WEB view for registration, view uses 3 forms, base RegistrationForm, PersonForm and PassportForm."""
    forms = {
        'user': RegistrationForm(),
        'person': PersonForm(),
        'passport': PassportForm()
    }

    def get(self, request, *args, **kwargs):
        """ If user is authenticated, redirect him to home."""
        if request.user.is_authenticated:
            return redirect('travelling_companion:home')
        return render(request, 'registration/register.html', {'forms': self.forms})

    def post(self, request, *args, **kwargs):
        """ First validate forms, then save all 3 forms. If any of forms not valid, generate error_ids and go back."""
        user = RegistrationForm(request.POST)
        person = PersonForm(request.POST)
        passport = PassportForm(request.POST)
        if user.is_valid() and person.is_valid() and passport.is_valid():
            new_user = user.save()

            new_person = person.save(commit=False)
            new_person.user_id = new_user.id
            new_person.created_by = new_user

            new_passport = passport.save(commit=False)
            new_passport.created_by = new_user
            new_passport.save()
            new_person.passport = new_passport
            new_person.save()

            messages.success(request, 'You have successfully registered, you can now log in')
            return redirect('mind_auth:login')
        self.forms = {
            'user': RegistrationForm(request.POST),
            'person': PersonForm(request.POST),
            'passport': PassportForm(request.POST)
        }
        error_ids = self.__get_error_ids(self.forms['user'])
        error_ids += self.__get_error_ids(self.forms['person'])
        error_ids += self.__get_error_ids(self.forms['passport'])
        return render(request, 'registration/register.html', {'forms': self.forms, 'error_ids': error_ids})

    @staticmethod
    def __get_error_ids(form):
        """ help method getting widget id's with errors, for JS to show bootstrap design for error fields."""
        return [form.fields[i].widget.attrs['id'] for i in form.errors.as_data()]
