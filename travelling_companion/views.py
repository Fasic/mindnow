from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import ListView, DeleteView, CreateView, UpdateView, DetailView

from travelling_companion.forms import TripForm, LocationForm, PersonWithPassportForm, PassportForm, CostItemForm, \
    FlightForm, AccommodationForm
from travelling_companion.models import Trip, Location, Person, Passport, TripPerson, CostItem, Flight, \
    TripAccommodation
from travelling_companion.permissions import CreatorPermissionMixin, CreatorOrPersonPermissionMixin, \
    CreatorOrInTripPermissionMixin, PersonPermissionMixin


class TripListView(LoginRequiredMixin, ListView):
    """
    TripListView, home page, with overview of trips.
    queryset: returns created_by trips for auth user, and trips auth user is part of.
    get_context_data: adds context for rendering not accepted trips for auth user.
    """
    model = Trip
    template_name = "travelling_companion/home.html"

    # paginate_by = 100

    def get_queryset(self):
        trips = TripPerson.objects.filter(person__user=self.request.user, approved=True) \
            .values_list('trip_id', flat=True)
        return Trip.objects.filter(Q(created_by=self.request.user) | Q(id__in=trips))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['not_accepted'] = TripPerson.objects.filter(
            person__user=self.request.user,
            accepted=False).values_list('trip_id', flat=True)
        return context


class TripDetailView(CreatorOrInTripPermissionMixin, DetailView):
    """
    TripDetailView, view for showing trip detail.
    get_context_data: adding context for rendering:
        1. trip_persons - Persons that are part of trip.
        2. persons - Persons that can be added to trip by auth user. TODO: add users, that are friends
        3. cost - All CostItems for trip
        4. fight - All flights on trip
        5. accommodation - All TripAccommodations for trip
        6. can_actions - boolean cat auth-user do actions on trip object
    """
    model = Trip

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['trip_persons'] = TripPerson.objects.filter(trip=self.object)
        context['persons'] = Person.objects.filter(created_by=self.request.user).exclude(tripperson__trip=self.object)
        context['cost'] = CostItem.objects.filter(trip=self.object)
        context['flight'] = Flight.objects.filter(trip=self.object)
        context['accommodation'] = TripAccommodation.objects.filter(trip=self.object)
        context['can_actions'] = TripPerson.objects.filter(
            trip=self.object,
            person__user=self.request.user,
            approved=True,
            accepted=True).count() > 0 or self.object.created_by == self.request.user
        return context


class TripDeleteView(CreatorPermissionMixin, DeleteView):
    model = Trip
    success_url = reverse_lazy('travelling_companion:home')
    template_name = 'travelling_companion/confirm_delete.html'


class TripCreateView(CreateView):
    """
    TripCreateView, view for creating trip.
    form_valid: override method, adding created_by value for auth user.
    get_form: override method, filtering "trip_location" field by owner.
    """
    model = Trip
    form_class = TripForm
    success_url = reverse_lazy('travelling_companion:home')
    template_name = 'travelling_companion/form.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def get_form(self, form_class=None):
        form = super().get_form()
        form.fields["trip_location"].queryset = Location.objects.filter(created_by=self.request.user)
        form.user = self.request.user
        return form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = context['form']
        context['error_ids'] = [f"id_{i}" for i in form.errors.as_data()]
        return context


class TripUpdateView(CreatorPermissionMixin, UpdateView):
    """
    TripUpdateView, view for updating trip.
    form_valid: override method, adding created_by value for auth user.
    get_form: override method, filtering "trip_location" field by owner.
    """
    model = Trip
    form_class = TripForm
    success_url = reverse_lazy('travelling_companion:home')
    template_name = 'travelling_companion/form.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def get_form(self, form_class=None):
        form = super().get_form()
        form.fields["trip_location"].queryset = Location.objects.filter(created_by=self.request.user)
        form.user = self.request.user
        return form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = context['form']
        context['error_ids'] = [f"id_{i}" for i in form.errors.as_data()]
        return context


class LocationView(CreateView):
    """
    LocationView, view for creating location (City).
    form_valid: override method, adding created_by value for auth user.
    get_form: override method, filtering "locations" field by owner (created_by).
    """
    template_name = 'travelling_companion/location_form.html'
    success_url = reverse_lazy('travelling_companion:location_form')
    form_class = LocationForm

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        messages.success(self.request, "Location successfully edited.")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['locations'] = Location.objects.filter(created_by=self.request.user)
        form = context['form']
        context['error_ids'] = [f"id_{i}" for i in form.errors.as_data()]
        return context


class LocationEditView(CreatorPermissionMixin, UpdateView):
    """
    LocationEditView, view for updating location (City).
    form_valid: override method, adding created_by value for auth user.
    get_form: override method, filtering "locations" field by owner (created_by).
    """
    model = Location
    template_name = 'travelling_companion/location_form.html'
    success_url = reverse_lazy('travelling_companion:location_form')
    form_class = LocationForm

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        messages.success(self.request, "Location successfully added.")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['locations'] = Location.objects.filter(created_by=self.request.user)
        form = context['form']
        context['error_ids'] = [f"id_{i}" for i in form.errors.as_data()]
        return context


class LocationDelete(CreatorPermissionMixin, View):
    model = Location

    def get(self, request, pk):
        location = get_object_or_404(Location, pk=pk)
        location.delete()
        messages.success(self.request, "Location successfully deleted.")
        return redirect(reverse_lazy('travelling_companion:location_form'))


class PersonListView(LoginRequiredMixin, ListView):
    """
    PersonListView, page showing all persons created by auth user.
    Pagination can be added by "paginate_by = x"
    """
    model = Person

    def get_queryset(self):
        return Person.objects.filter(created_by=self.request.user)


class PersonDeleteView(CreatorPermissionMixin, DeleteView):
    model = Person
    success_url = reverse_lazy('travelling_companion:person_list')
    template_name = 'travelling_companion/confirm_delete.html'


class PersonCreateView(CreateView):
    """
    PersonCreateView, view for creating person (person that can't login to APP).
    form_valid: override method, adding created_by value for auth user.
    get_form: override method, filtering "passport" field by owner (created_by)
    and passports which do not belong to anyone.
    """
    model = Person
    form_class = PersonWithPassportForm
    success_url = reverse_lazy('travelling_companion:person_list')
    template_name = 'travelling_companion/form.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def get_form(self, form_class=None):
        form = super().get_form()
        form.fields["passport"].queryset = Passport.objects.filter(
            Q(created_by=self.request.user) &
            Q(person=None) | Q(person=self.object))
        return form


class PersonUpdateView(CreatorPermissionMixin, UpdateView):
    """
    PersonUpdateView, view for updating person (person that can't login to APP).
    form_valid: override method, adding created_by value for auth user.
    get_form: override method, filtering "passport" field by owner (created_by)
    and passports which do not belong to anyone.
    """

    model = Person
    form_class = PersonWithPassportForm
    template_name = 'travelling_companion/form.html'
    success_url = reverse_lazy('travelling_companion:person_list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def get_form(self, form_class=None):
        form = super().get_form()
        form.fields["passport"].queryset = Passport.objects.filter(
            Q(created_by=self.request.user) &
            Q(person=None) | Q(person=self.object))
        return form


class PassportCreateView(CreateView):
    """
    PassportCreateView, view for creating passport for person.
    form_valid: override method, adding created_by value for auth user.
    """
    template_name = 'travelling_companion/form.html'
    success_url = reverse_lazy('travelling_companion:person_list')
    form_class = PassportForm

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = context['form']
        context['error_ids'] = [f"id_{i}" for i in form.errors.as_data()]
        return context


class CostView(CreateView):
    """
    CostView, view for creating CostItem.
    form_valid: override method, adding trip value for object.
    post: override method, generating success_url and trip, from trip_id.
    """
    template_name = 'travelling_companion/form.html'
    success_url = reverse_lazy('travelling_companion:home')
    form_class = CostItemForm

    def form_valid(self, form):
        form.instance.trip = self.trip
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        self.success_url = reverse('travelling_companion:trip_detail', args=(kwargs['trip_id'],))
        self.trip = get_object_or_404(Trip, pk=kwargs['trip_id'])
        return super().post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = context['form']
        context['error_ids'] = [f"id_{i}" for i in form.errors.as_data()]
        return context


class CostEditView(CreatorOrInTripPermissionMixin, UpdateView):
    """
    CostView, view for updating CostItem.
    post: override method, generating success_url and trip, from trip_id.
    """
    model = CostItem
    template_name = 'travelling_companion/form.html'
    success_url = reverse_lazy('travelling_companion:home')
    form_class = CostItemForm
    trip = None

    def post(self, request, *args, **kwargs):
        self.success_url = reverse('travelling_companion:trip_detail', args=(kwargs['trip_id'],))
        self.trip = get_object_or_404(Trip, pk=kwargs['trip_id'])
        return super().post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = context['form']
        context['error_ids'] = [f"id_{i}" for i in form.errors.as_data()]
        return context


class CostDelete(CreatorOrInTripPermissionMixin, View):
    model = CostItem

    def get(self, request, pk):
        cost = get_object_or_404(CostItem, pk=pk)
        cost.delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


class FlightView(View):
    """ FlightView, view for creating Flight. """
    template_name = 'travelling_companion/form.html'

    def get(self, request, trip_id):
        """ Filtering  fields by requast.user and trip_id. """
        form = FlightForm()
        locations = Location.objects.filter(created_by=self.request.user)
        form.fields["from_dest"].queryset = locations
        form.fields["to_dest"].queryset = locations
        form.fields["cost"].queryset = CostItem.objects.filter(trip_id=trip_id)
        return render(request, self.template_name, {'form': form})

    def post(self, request, trip_id):
        """ Saving flight object. """
        form = FlightForm(request.POST)
        if form.is_valid():
            flight = form.save(commit=False)
            flight.trip = Trip.objects.get(pk=trip_id)
            flight.save()
            return HttpResponseRedirect(reverse('travelling_companion:trip_detail', args=(trip_id,)))
        context = {'form': form, 'error_ids': [f"id_{i}" for i in form.errors.as_data()]}
        return render(request, self.template_name, context)


class FlightEditView(CreatorOrInTripPermissionMixin, View):
    """ FlightEditView, view for updating Flight. """
    template_name = 'travelling_companion/form.html'
    model = Flight

    def get(self, request, pk, trip_id):
        """ Filtering  fields by requast.user and trip_id. """
        form = FlightForm(instance=Flight.objects.get(pk=pk))
        locations = Location.objects.filter(created_by=self.request.user)
        form.fields["from_dest"].queryset = locations
        form.fields["to_dest"].queryset = locations
        form.fields["cost"].queryset = CostItem.objects.filter(trip_id=trip_id)
        return render(request, self.template_name, {'form': form})

    def post(self, request, pk, trip_id):
        """ Saving flight object. """
        form = FlightForm(request.POST or None, instance=Flight.objects.get(pk=pk))
        if form.is_valid():
            flight = form.save(commit=False)
            flight.trip = Trip.objects.get(pk=trip_id)
            flight.save()
            return HttpResponseRedirect(reverse('travelling_companion:trip_detail', args=(trip_id,)))
        context = {'form': form, 'error_ids': [f"id_{i}" for i in form.errors.as_data()]}
        return render(request, self.template_name, context)


class FlightDelete(CreatorOrInTripPermissionMixin, View):
    """ FlightDelete, view for deleting Flight. Model is used for permissions. """
    model = Flight

    def get(self, request, pk):
        """ First delete cost object, then delete flight. """
        flight = get_object_or_404(Flight, pk=pk)
        if flight.cost:
            flight.cost.delete()
        flight.delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


class AccommodationView(View):
    """ AccommodationView, view for creating TripAccommodation. """
    template_name = 'travelling_companion/form.html'

    def get(self, request, trip_id):
        """ Filtering  fields by requast.user and trip_id. """
        form = AccommodationForm()
        form.fields["location"].queryset = Location.objects.filter(created_by=self.request.user)
        form.fields["cost"].queryset = CostItem.objects.filter(trip_id=trip_id)
        return render(request, self.template_name, {'form': form})

    def post(self, request, trip_id):
        """ Saving accommodation object. """
        form = AccommodationForm(request.POST)
        if form.is_valid():
            accom = form.save(commit=False)
            accom.trip = Trip.objects.get(pk=trip_id)
            accom.save()
            return HttpResponseRedirect(reverse('travelling_companion:trip_detail', args=(trip_id,)))
        context = {'form': form, 'error_ids': [f"id_{i}" for i in form.errors.as_data()]}
        return render(request, self.template_name, context)


class AccommodationEditView(CreatorOrInTripPermissionMixin, View):
    """ AccommodationView, view for updating TripAccommodation. """
    template_name = 'travelling_companion/form.html'
    model = TripAccommodation

    def get(self, request, pk, trip_id):
        """ Filtering  fields by requast.user and trip_id. """
        form = AccommodationForm(instance=TripAccommodation.objects.get(pk=pk))
        form.fields["location"].queryset = Location.objects.filter(created_by=self.request.user)
        form.fields["cost"].queryset = CostItem.objects.filter(trip_id=trip_id)
        return render(request, self.template_name, {'form': form})

    def post(self, request, pk, trip_id):
        """ Saving accommodation object. """
        form = AccommodationForm(request.POST or None, instance=TripAccommodation.objects.get(pk=pk))
        if form.is_valid():
            accom = form.save(commit=False)
            accom.trip = Trip.objects.get(pk=trip_id)
            accom.save()
            return HttpResponseRedirect(reverse('travelling_companion:trip_detail', args=(trip_id,)))
        context = {'form': form, 'error_ids': [f"id_{i}" for i in form.errors.as_data()]}
        return render(request, self.template_name, context)


class AccommodationDelete(CreatorOrInTripPermissionMixin, View):
    """ AccommodationDelete, view for deleting accommodation. Model is used for permissions. """
    model = TripAccommodation

    def get(self, request, pk):
        """ First delete cost object, then delete accommodation. """
        accom = get_object_or_404(TripAccommodation, pk=pk)
        if accom.cost:
            accom.cost.delete()
        accom.delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


class AccepteTrip(PersonPermissionMixin, View):
    """ AcceptTrip, view for accepting trip by called user. Model is used for permissions. """
    model = Trip

    def get(self, request, pk):
        trip_request = TripPerson.objects.filter(trip_id=pk, accepted=False, person__user=request.user).first()
        if not trip_request:
            return HttpResponse(status=400)
        if trip_request.accepted:
            return HttpResponse(status=304)
        trip_request.accepted = True
        trip_request.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


class ApproveTrip(CreatorPermissionMixin, View):
    """ ApproveTrip, view for trip approval by trip host. Model is used for permissions. """
    model = Trip

    def get(self, request, pk):
        trip_request = TripPerson.objects.filter(trip_id=pk, approved=False, trip__created_by=request.user).first()
        if not trip_request:
            return HttpResponse(status=400)
        if trip_request.approved:
            return HttpResponse(status=304)
        trip_request.approved = True
        trip_request.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


class AddPersonTrip(CreatorOrInTripPermissionMixin, View):
    """ AddPersonTrip, view for adding person to trip. Model is used for permissions. """
    model = Trip

    def get(self, request, person_id, pk):
        """ Validate that person is free at time of travel if not output error msg,
        Before save, set accepted and approved by user type, and request.user role. """
        trip = get_object_or_404(Trip, pk=pk)
        person = get_object_or_404(Person, pk=person_id)
        if person in TripPerson.objects.filter(trip=trip):
            return HttpResponse(status=304)

        if self.isPersonNotFree(trip, person):
            messages.error(request, "Cant add user. User not free at time.")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

        trip_person = TripPerson()
        trip_person.person = person
        trip_person.trip = trip
        if trip.created_by != request.user:
            trip_person.approved = False
        if person.user:
            trip_person.accepted = False
        trip_person.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

    def isPersonNotFree(self, trip, person):
        from_date = trip.from_date
        to_date = trip.to_date

        trips = Trip.objects.filter(tripperson__person=person)
        not_free = trips.filter(from_date__lt=from_date, to_date__gt=from_date).count() != 0 \
                   or trips.filter(from_date__lt=to_date, to_date__gt=to_date).count() != 0 \
                   or trips.filter(from_date__gte=from_date, to_date__lte=to_date).count() != 0
        return not_free


class RemovePersonTrip(CreatorOrPersonPermissionMixin, View):
    """ RemovePersonTrip, view for removing person from trip. Model is used for permissions. """
    model = TripPerson

    def get(self, request, pk):
        """ Redirecting user to right page, if user is not part of trip, redirect to home, else redirect back. """
        trip_person = get_object_or_404(TripPerson, pk=pk)
        if trip_person.trip.created_by != request.user and trip_person.person.user != request.user:
            return HttpResponse(status=400)
        trip_person.delete()
        if trip_person.person.user == request.user and trip_person.trip.created_by != request.user:
            return HttpResponseRedirect(reverse('travelling_companion:home'))
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
