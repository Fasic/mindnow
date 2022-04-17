from django.contrib.auth.models import User
from django.db import models
from django.conf import settings


class Location(models.Model):
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Passport(models.Model):
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    passport_number = models.CharField(max_length=20, unique=True)  # Todo: secure this, with encription
    date_issued = models.DateField()
    valid_until = models.DateField()

    def __str__(self):
        return f"{self.passport_number} ({self.date_issued} - {self.valid_until})"


class Person(models.Model):
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="created_by")
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    passport = models.OneToOneField(Passport, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Trip(models.Model):
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.CharField(max_length=200, null=True, blank=True)
    from_date = models.DateField()
    to_date = models.DateField()
    budget = models.FloatField(default=0)
    trip_location = models.ManyToManyField(Location, blank=True)

    def __str__(self):
        return f"{self.description} ({self.from_date}-{self.to_date})"

    def total_spending(self):
        """Method that calculates total trip expenses."""
        return sum([item.price for item in self.costitem_set.all()])

    def budget_limit(self):
        """Method that calculates total 75% of budget, as "limit"."""
        return self.budget * 0.75


class TripPerson(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    accepted = models.BooleanField(default=True)  # when user is added, he must accept req.
    approved = models.BooleanField(default=True)  # if someone adds someone else, owner must approve it

    def __str__(self):
        return f"{self.person}"


class UserRelationships(models.Model):
    user1 = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    user2 = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="recipient")
    request_time = models.DateTimeField(auto_now_add=True)
    accepted = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user1', 'user2')

    def __str__(self):
        return f"{self.user1} - {self.user2} ({self.accepted})"


class CostItem(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    description = models.CharField(max_length=200, null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.description} ({self.price})"


class Flight(models.Model):
    # flight related data
    flight_number = models.CharField(max_length=20)
    confirmation_code = models.CharField(max_length=10)

    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    from_dest = models.ForeignKey(Location, on_delete=models.SET_NULL, related_name="from_dest", null=True)
    to_dest = models.ForeignKey(Location, on_delete=models.SET_NULL, related_name="to_dest", null=True)
    flight_time = models.DateTimeField()
    checked = models.BooleanField(default=False)
    cost = models.ForeignKey(CostItem, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.trip}: {self.from_dest}  - {self.to_dest} ({self.flight_time})"


class TripAccommodation(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    from_date = models.DateField()
    to_date = models.DateField()
    cost = models.ForeignKey(CostItem, on_delete=models.SET_NULL, null=True, blank=True)

    # booking data
    # address = models.CharField(max_length=100, null=True, blank=True)
    # phone = models.CharField(max_length=20, null=True, blank=True)
    # check_in = models.CharField(max_length=100, null=True, blank=True)
    # check_out = models.CharField(max_length=100, null=True, blank=True)
    # confirmation_number = models.CharField(max_length=10, null=True, blank=True)
    # pin = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return f"{self.trip}: {self.location}"
