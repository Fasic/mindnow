from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework import generics, mixins, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from rest_api.permissions import IsOwner, IsTripOwner, IsTraveler, InRelation
from rest_api.serializers import TripSerializer, PersonSerializer, PassportSerializer, \
    RelationshipsSerializer, LocationSerializer, TripPersonSerializer, CostItemSerializer, FlightSerializer, \
    TripAccommodationSerializer
from travelling_companion.models import Trip, Person, Passport, UserRelationships, TripPerson, Location, CostItem, \
    Flight, TripAccommodation


class TripList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    """API: Get list of trips and adding new trip via post,
     permissions: User need to be authenticated, and owner of object."""
    serializer_class = TripSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        """overriding method to add filter for trips, trips user can get:
        created by auth user or user is traveler in trip (approved and accepted)."""
        trips = TripPerson.objects.filter(person__user=self.request.user.id, approved=True, accepted=True) \
            .values_list('trip_id', flat=True)
        return Trip.objects.filter(Q(created_by_id=self.request.user.id) | Q(pk__in=trips))

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """Add created_by as current user."""
        request.data['created_by'] = self.request.user.id
        return self.create(request, *args, **kwargs)


class TripDetail(generics.RetrieveUpdateDestroyAPIView):
    """API: Get Update Delete Trip object,
     permissions: User need to be authenticated, and owner of object."""
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def put(self, request, *args, **kwargs):
        """Add created_by as current user."""
        request.data['created_by'] = self.request.user.id
        return self.update(request, *args, **kwargs)


class LocationList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    """API: Get list of locations and adding new location via post,
     permissions: User need to be authenticated, and owner of object."""
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        return Location.objects.filter(created_by=self.request.user.id)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """Add created_by as current user."""
        request.data['created_by'] = self.request.user.id
        return self.create(request, *args, **kwargs)


class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
    """API: Get Update Delete Location object,
     permissions: User need to be authenticated, and owner of object."""
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def put(self, request, *args, **kwargs):
        """Add created_by as current user."""
        request.data['created_by'] = self.request.user.id
        return self.update(request, *args, **kwargs)


class PersonList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    """API: Get list of Persons and adding new person via post,
     permissions: User need to be authenticated, and owner of object."""
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        return Person.objects.filter(Q(user=self.request.user.id) | Q(created_by=self.request.user.id))

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """Add created_by as current user."""
        request.data['created_by'] = self.request.user.id
        return self.create(request, *args, **kwargs)


class PersonDetail(generics.RetrieveUpdateDestroyAPIView):
    """API: Get Update Delete Person object,
     permissions: User need to be authenticated, and owner of object."""
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def put(self, request, *args, **kwargs):
        """Add created_by as current user."""
        request.data['created_by'] = self.request.user.id
        return self.update(request, *args, **kwargs)


class PassportList(mixins.ListModelMixin, generics.GenericAPIView):
    """API: Get list of Passports,
     permissions: User need to be authenticated, and owner of object."""
    queryset = Passport.objects.all()
    serializer_class = PassportSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        return Passport.objects.filter(created_by=self.request.user.id)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class PassportCreate(mixins.CreateModelMixin, generics.GenericAPIView):
    """API: Adding new Passport object, passport is added to person via person.id,
     permissions: User need to be authenticated, and owner of object."""
    serializer_class = PassportSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def post(self, request, *args, **kwargs):
        """Add created_by as current user."""
        request.data['created_by'] = self.request.user.id
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        """Add passport to a user."""
        person = get_object_or_404(Person, pk=self.kwargs['id'])
        instance = serializer.save()
        person.passport = instance
        person.save()


class PassportDetail(generics.RetrieveUpdateDestroyAPIView):
    """API: Get Update Delete passport object,
     permissions: User need to be authenticated, and owner of object."""
    queryset = Passport.objects.all()
    serializer_class = PassportSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def put(self, request, *args, **kwargs):
        """Add created_by as current user."""
        request.data['created_by'] = self.request.user.id
        return self.update(request, *args, **kwargs)


class TripPersonList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    """API: Get list of TripPersons and adding new Person to trip via post,
     permissions: User need to be authenticated, and owner of object."""
    queryset = TripPerson.objects.all()
    serializer_class = TripPersonSerializer
    permission_classes = [IsAuthenticated, IsTripOwner | IsTraveler]

    def get_queryset(self):
        """filter trip persons for trips created_by current user or trips current user is traveler."""
        return TripPerson.objects.filter(
            Q(trip__created_by=self.request.user.id) | Q(traveler__user_id=self.request.user.id))

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """Create trip_person object, for trip and person, and update accepted/approved values
        depending on the person and trip host."""
        trip = get_object_or_404(Trip, pk=request.data['trip'])
        person = get_object_or_404(Person, pk=request.data['traveler'])

        if trip.created_by == self.request.user and person.user:
            request.data['accepted'] = False
        else:
            request.data['approved'] = False
            if person.user:
                request.data['accepted'] = False
        return self.create(request, *args, **kwargs)


class TripPersonDetail(generics.RetrieveUpdateDestroyAPIView):
    """API: Get Update Delete TripPerson object,
     permissions: User need to be authenticated, and owner of object."""
    queryset = TripPerson.objects.all()
    serializer_class = TripPersonSerializer
    permission_classes = [IsAuthenticated, IsTripOwner | IsTraveler]


class RelationshipsList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    """API: Get list of Relationships between users and adding new Relationships via post,
     permissions: User need to be authenticated, or InRelation of object."""
    queryset = UserRelationships.objects.all()
    serializer_class = RelationshipsSerializer
    permission_classes = [IsAuthenticated, InRelation]

    def get_queryset(self):
        """filter relationships, curent user must be recipient or sender of request."""
        return UserRelationships.objects.filter(Q(user1_id=self.request.user.id) | Q(user2_id=self.request.user.id))

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class RelationshipsDetail(generics.RetrieveUpdateDestroyAPIView):
    """API: Get Update Delete Relationships between users,
     permissions: User need to be authenticated, or InRelation of object."""
    queryset = UserRelationships.objects.all()
    serializer_class = RelationshipsSerializer
    permission_classes = [IsAuthenticated, InRelation]


class CostItemList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    """API: Get list of CostItems for trip and adding new CostItem via post,
     permissions: User need to be authenticated, and IsTripOwner or IsTraveler(trip)."""
    queryset = CostItem.objects.all()
    serializer_class = CostItemSerializer
    permission_classes = [IsAuthenticated, IsTripOwner | IsTraveler]

    def get_queryset(self):
        """filter CostItems by trips, CostItem for trips user can get:
        trips created by current user or user is traveler in trip (approved and accepted)."""
        trips = TripPerson.objects.filter(person__user=self.request.user.id, approved=True, accepted=True) \
            .values_list('trip_id', flat=True)
        return CostItem.objects.filter(Q(trip__created_by=self.request.user.id) | Q(trip__in=trips))

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CostItemDetail(generics.RetrieveUpdateDestroyAPIView):
    """API: Get Update Delete CostItem for trip,
     permissions: User need to be authenticated, and IsTripOwner or IsTraveler(trip)."""
    queryset = CostItem.objects.all()
    serializer_class = CostItemSerializer
    permission_classes = [IsAuthenticated, IsTripOwner | IsTraveler]


class FlightList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    """API: Get list of Flights for trip and adding new Flight via post,
     permissions: User need to be authenticated, and IsTripOwner or IsTraveler(trip)."""
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = [IsAuthenticated, IsTripOwner | IsTraveler]

    def get_queryset(self):
        """filter Flights by trips, Flights for trips user can get:
        trips created by current user or user is traveler in trip (approved and accepted)."""
        trips = TripPerson.objects.filter(person__user=self.request.user.id, approved=True, accepted=True) \
            .values_list('trip_id', flat=True)
        return Flight.objects.filter(Q(trip__created_by=self.request.user.id) | Q(trip__in=trips))

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """Automatically add CostItem for Flight"""
        if 'price' in request.data:
            cost = CostItem()
            cost.price = request.data['price']
            cost.trip = Trip.objects.get(pk=request.data['trip'])
            cost.save()
            request.data['cost'] = cost.id
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        """Add cost item to object and change description."""
        instance = serializer.save()
        if instance.cost:
            instance.cost.description = "Flight:" + str(instance)
            instance.cost.save()


class FlightDetail(generics.RetrieveUpdateDestroyAPIView):
    """API: Get Update Delete Flights for trip,
     permissions: User need to be authenticated, and IsTripOwner or IsTraveler(trip)."""
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = [IsAuthenticated, IsTripOwner | IsTraveler]


class TripAccommodationList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    """API: Get list of Accommodations for trip and adding new Accommodation via post,
     permissions: User need to be authenticated, and IsTripOwner or IsTraveler(trip)."""
    queryset = TripAccommodation.objects.all()
    serializer_class = TripAccommodationSerializer
    permission_classes = [IsAuthenticated, IsTripOwner | IsTraveler]

    def get_queryset(self):
        """filter Accommodations by trips, Accommodations for trips user can get:
        trips created by current user or user is traveler in trip (approved and accepted)."""
        trips = TripPerson.objects.filter(person__user=self.request.user.id, approved=True, accepted=True) \
            .values_list('trip_id', flat=True)
        return TripAccommodation.objects.filter(Q(trip__created_by=self.request.user.id) | Q(trip__in=trips))

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """Automatically add cost for Accommodation"""
        if 'price' in request.data:
            cost = CostItem()
            cost.price = request.data['price']
            cost.trip = Trip.objects.get(pk=request.data['trip'])
            cost.save()
            request.data['cost'] = cost.id
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        """Add cost item to object and change description."""
        instance = serializer.save()
        if instance.cost:
            instance.cost.description = "Booking:" + str(instance)
            instance.cost.save()


class TripAccommodationDetail(generics.RetrieveUpdateDestroyAPIView):
    """API: Get Update Delete Accommodations for trip,
     permissions: User need to be authenticated, and IsTripOwner or IsTraveler(trip)."""
    queryset = TripAccommodation.objects.all()
    serializer_class = TripAccommodationSerializer
    permission_classes = [IsAuthenticated, IsTripOwner | IsTraveler]


@api_view()
@login_required
def accept_relationship(request, pk):
    """ accept_relationship, view for accepting relationship between users. Auth user must be recipient in relationship
        and relationship must not be accepted."""
    relationship = get_object_or_404(UserRelationships, pk=pk)
    if relationship.user2 != request.user:
        return Response("Not your request.", status=status.HTTP_400_BAD_REQUEST)
    if relationship.accepted:
        return Response("The request has already been accepted.", status=status.HTTP_304_NOT_MODIFIED)
    relationship.accepted = True
    relationship.save()
    return Response("Request accepted.", status=status.HTTP_202_ACCEPTED)


@api_view()
@login_required
def accept_trip(request, pk):
    """ accept_trip, view for accepting trip by called user. Auth user must be person in trip_request
        and trip_request must not be accepted."""
    trip_request = get_object_or_404(TripPerson, pk=pk)
    if trip_request.person.user != request.user:
        return Response("Not your request.", status=status.HTTP_400_BAD_REQUEST)
    if trip_request.accepted:
        return Response("The request has already been accepted.", status=status.HTTP_304_NOT_MODIFIED)
    trip_request.accepted = True
    trip_request.save()
    return Response("Request accepted.", status=status.HTTP_202_ACCEPTED)


@api_view()
@login_required
def approve_trip(request, pk):
    """ approve_trip, view for approval of travel person by trip host. Auth user must be trip host
        and trip_request must not be approved."""
    trip_request = get_object_or_404(TripPerson, pk=pk)
    if trip_request.trip.created_by != request.user:
        return Response("Not your request.", status=status.HTTP_400_BAD_REQUEST)
    if trip_request.approved:
        return Response("The request has already been approved.", status=status.HTTP_304_NOT_MODIFIED)
    trip_request.approved = True
    trip_request.save()
    return Response("Request approved.", status=status.HTTP_202_ACCEPTED)
