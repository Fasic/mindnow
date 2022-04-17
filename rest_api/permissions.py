from rest_framework import permissions

from travelling_companion.models import Trip, TripPerson


class ReadOnly(permissions.BasePermission):
    """ReadOnly permissions, user can call SAFE_METHODS only. ('GET', 'HEAD', 'OPTIONS')"""

    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS


class IsOwner(permissions.BasePermission):
    """Current user owner of object (created_by)."""

    def has_object_permission(self, request, view, obj):
        return obj.created_by == request.user


class IsTripOwner(permissions.BasePermission):
    """Current user must be owner of trip in object (created_by)."""

    def has_object_permission(self, request, view, obj):
        return obj.trip.created_by == request.user


class IsTraveler(permissions.BasePermission):
    """Current user must be trip traveler (approved+accepted)."""

    def has_object_permission(self, request, view, obj):
        trip = obj
        if type(obj) != Trip:
            trip = obj.trip
        return TripPerson.objects.filter(trip=trip, person__user=request.user, accepted=True, approved=True) > 0


class InRelation(permissions.BasePermission):
    """Current user must be InRelation (user1 or user2)."""

    def has_object_permission(self, request, view, obj):
        return obj.user1 == request.user or obj.user2 == request.user
