from django.contrib.auth.mixins import UserPassesTestMixin

from travelling_companion.models import Trip, TripPerson, Location, Person


class CreatorPermissionMixin(UserPassesTestMixin):
    """
    CreatorPermissionMixin, permission checking is request.user owner of object.
    types is list of supported model types. The model must have a field "created_by",
    or permission returns False.
    """

    def test_func(self):
        types = [Trip, Location, Person]

        obj = self.model.objects.get(pk=self.kwargs['pk'])
        if type(obj) not in types:
            return False
        return obj.created_by == self.request.user


class CreatorOrInTripPermissionMixin(UserPassesTestMixin):
    """
    CreatorOrInTripPermissionMixin, permission checking is request.user owner of object or
    request.user is in trip and he has "approved" status.
    Model must be Trip, or must have trip object.
    """

    def test_func(self):
        obj = self.model.objects.get(pk=self.kwargs['pk'])
        if type(obj) == Trip:
            trip_users = TripPerson.objects.filter(trip_id=obj.id, approved=True).values_list('person__user', flat=True)
            return obj.created_by == self.request.user or self.request.user.id in trip_users
        trip_users = TripPerson.objects.filter(trip_id=obj.trip.id, approved=True).values_list('person__user',
                                                                                               flat=True)
        return obj.trip.created_by == self.request.user or self.request.user.id in trip_users


class CreatorOrPersonPermissionMixin(UserPassesTestMixin):
    """
    CreatorOrPersonPermissionMixin, permission checking is request.user owner of object or
    request.user is person in object.
    Model must be TripPerson.
    """

    def test_func(self):
        obj = self.model.objects.get(pk=self.kwargs['pk'])
        if type(obj) == TripPerson:
            return obj.person.user == self.request.user or obj.trip.created_by == self.request.user


class PersonPermissionMixin(UserPassesTestMixin):
    """
    PersonPermissionMixin, permission checking request.user is person in TripPerson object,
    which is associated with trip. Self must have pk of Trip.
    """

    def test_func(self):
        return TripPerson.objects.filter(
            trip_id=self.kwargs['pk'],
            accepted=False,
            person__user=self.request.user).count() > 0
