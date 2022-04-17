from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import ModelForm

# from travelling_companion.models import Traveler
from travelling_companion.models import Person, Trip, Location, Passport, CostItem, Flight, TripAccommodation, \
    TripPerson


class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(
        label='Password',
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'current-password',
                'class': 'form-control',
                'placeholder': 'Password',
                'id': 'Password1'
            }
        ),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label='Confirm password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Confirm Password',
                'id': 'Password2'
            }
        ),
        strip=False,
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email')
        field_classes = {'username': UsernameField}
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'placeholder': 'Username',
                    'id': 'username',
                    'class': 'form-control form-control-line'
                }),
            'email': forms.TextInput(
                attrs={
                    'placeholder': 'Email',
                    'id': 'email',
                    'class': 'form-control form-control-line'
                })
        }


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
        exclude = ('user', 'created_by', 'passport')
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Name',
                    'id': 'first_name',
                    'class': 'form-control form-control-line',
                    'autofocus': 'autofocus'
                }),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Last name',
                    'id': 'last_name',
                    'class': 'form-control form-control-line'
                })
        }


class PersonWithPassportForm(ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
        exclude = ('user', 'created_by')
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Name',
                    'id': 'first_name',
                    'class': 'form-control form-control-line',
                    'autofocus': 'autofocus'
                }),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Last name',
                    'id': 'last_name',
                    'class': 'form-control form-control-line'
                }),
            'passport': forms.Select(
                attrs={
                    'class': 'form-control form-control-line'
                })
        }


class PassportForm(ModelForm):
    class Meta:
        model = Passport
        fields = '__all__'
        exclude = ('created_by',)
        widgets = {
            'passport_number': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Passport number',
                },
            ),
            'date_issued': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Valid until',
                    'type': 'date'
                }
            ),
            'valid_until': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Date issued',
                    'type': 'date'
                }
            ),
        }


class TripForm(ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = None
        super().__init__(*args, **kwargs)

    class Meta:
        model = Trip
        fields = '__all__'
        exclude = ('created_by',)
        widgets = {
            'description': forms.TextInput(
                attrs={
                    'placeholder': 'Description',
                    'class': 'form-control form-control-line',
                    'autofocus': 'autofocus'
                }),
            'from_date': forms.DateInput(attrs={'class': 'form-control form-control-line', 'type': 'date'}),
            'to_date': forms.DateInput(attrs={'class': 'form-control form-control-line', 'type': 'date'}),
            'budget': forms.NumberInput(attrs={'class': 'form-control form-control-line', 'type': 'decimal'}),
            'trip_location': forms.SelectMultiple(attrs={'class': 'form-select'})
        }

    def clean(self):
        cleaned_data = super().clean()
        from_date = cleaned_data.get("from_date")
        to_date = cleaned_data.get("to_date")

        trips = Trip.objects.filter(created_by=self.user)
        from_date_invalid = trips.filter(from_date__lt=from_date, to_date__gt=from_date).count() != 0
        to_date_invalid = trips.filter(from_date__lt=to_date, to_date__gt=to_date).count() != 0
        both_invalid = trips.filter(from_date__gte=from_date, to_date__lte=to_date).count() != 0

        errors = {}
        if both_invalid:
            errors['from_date'] = "From date of trip overlap with your other trip."
            errors['to_date'] = "To date of trip overlap with your other trip."
        if from_date_invalid:
            errors['from_date'] = "From date of trip overlap with your other trip."
        if to_date_invalid:
            errors['to_date'] = "To date of trip overlap with your other trip."
        raise ValidationError(errors)


class LocationForm(ModelForm):
    class Meta:
        model = Location
        fields = '__all__'
        exclude = ('created_by',)
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Name',
                    'class': 'form-control form-control-line',
                    'autofocus': 'autofocus'
                })
        }


class CostItemForm(ModelForm):
    class Meta:
        model = CostItem
        fields = '__all__'
        exclude = ('trip',)
        widgets = {
            'description': forms.TextInput(
                attrs={
                    'placeholder': 'Description',
                    'class': 'form-control form-control-line',
                    'autofocus': 'autofocus'
                }),
            'price': forms.NumberInput(
                attrs={
                    'placeholder': 'Price',
                    'class': 'form-control form-control-line',
                })
        }


class FlightForm(ModelForm):
    class Meta:
        model = Flight
        fields = '__all__'
        exclude = ('trip',)
        widgets = {
            'flight_number': forms.TextInput(
                attrs={
                    'placeholder': 'Flight number',
                    'class': 'form-control form-control-line',
                    'autofocus': 'autofocus'
                }),
            'confirmation_code': forms.TextInput(
                attrs={'placeholder': 'Confirmation code', 'class': 'form-control form-control-line', }
            ),
            'flight_time': forms.DateTimeInput(
                format='%Y-%m-%d %H:%M:%S',
                attrs={
                    'class': 'date-time-field form-control form-control-line',
                    'type': 'datetime'
                }),
            'from_dest': forms.Select(attrs={'class': 'form-control form-control-line'}),
            'to_dest': forms.Select(attrs={'class': 'form-control form-control-line'}),
            'checked': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'cost': forms.Select(attrs={'class': 'form-control form-control-line'})
        }


class AccommodationForm(ModelForm):
    class Meta:
        model = TripAccommodation
        fields = '__all__'
        exclude = ('trip',)
        widgets = {
            'from_date': forms.DateInput(
                format='%Y-%m-%d',
                attrs={
                    'class': 'date-field form-control form-control-line',
                    'type': 'date'
                }),
            'to_date': forms.DateInput(
                format='%Y-%m-%d',
                attrs={
                    'class': 'date-field form-control form-control-line',
                    'type': 'date'
                }),
            'location': forms.Select(attrs={'class': 'form-control form-control-line'}),
            'cost': forms.Select(attrs={'class': 'form-control form-control-line'}),
        }
