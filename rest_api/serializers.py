from django.contrib.auth.decorators import login_required
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.authtoken.admin import User
from rest_framework.validators import UniqueTogetherValidator, UniqueValidator

from rest_api.validators import FreeTimeValidate, DateValidate
from travelling_companion.models import \
    Trip, Person, Passport, UserRelationships, Location, TripPerson, TripAccommodation, CostItem, Flight


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


class PassportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passport
        fields = '__all__'


class TripPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = TripPerson
        fields = '__all__'


class RelationshipsSerializer(serializers.ModelSerializer):
    def validate(self, data):
        """Validate user1 and user2, must not be the same."""
        if 'user1' in data and 'user2' in data:
            if data['user1'] == data['user2']:
                raise serializers.ValidationError("You can't send a request to yourself.")
        return data

    class Meta:
        """Validate user1 and user2, must be UniqueTogether."""
        model = UserRelationships
        fields = '__all__'

        validators = [
            UniqueTogetherValidator(
                queryset=UserRelationships.objects.all(),
                fields=['user1', 'user2']
            )
        ]


class TripSerializer(serializers.ModelSerializer):
    class Meta:
        """Validate Trip must not overlap with other trips."""
        model = Trip
        fields = '__all__'

        validators = [
            FreeTimeValidate(queryset=Trip.objects.all()),
            DateValidate()
        ]


class CostItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CostItem
        fields = '__all__'


class TripAccommodationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TripAccommodation
        fields = '__all__'


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password']


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        """Validate password's must match."""
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        """On create add person."""
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()

        person = Person.objects.create(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            created_by=user
        )
        person.save()

        return user
