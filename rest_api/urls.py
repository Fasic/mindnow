from django.urls import path, include

from mind_auth.views import UserList, RegisterView
from rest_api import views
from rest_framework.authtoken import views as auth_views

app_name = 'rest_api'
urlpatterns = [
    path('auth/users/', UserList.as_view(), name='users'),
    path('auth/auth_token/', auth_views.obtain_auth_token, name='auth_token'),
    path('auth/register/', RegisterView.as_view(), name='api_register'),

    path('trip/', views.TripList.as_view()),
    path('trip/<int:pk>/', views.TripDetail.as_view()),

    path('location/', views.LocationList.as_view(), name='location-list'),
    path('location/<int:pk>/', views.LocationDetail.as_view(), name='location-detail'),

    path('person/', views.PersonList.as_view()),
    path('person/<int:pk>/', views.PersonDetail.as_view()),

    path('passport/', views.PassportList.as_view()),
    path('passport/<int:pk>/', views.PassportDetail.as_view()),
    path('passport/create/<int:id>/', views.PassportCreate.as_view()),

    path('trip_persons/', views.TripPersonList.as_view()),
    path('trip_persons/<int:pk>/', views.TripPersonDetail.as_view()),

    path('relationships/', views.RelationshipsList.as_view()),
    path('relationships/<int:pk>/', views.RelationshipsDetail.as_view()),

    path('flight/', views.FlightList.as_view()),
    path('flight/<int:pk>/', views.FlightDetail.as_view()),

    path('accommodation/', views.TripAccommodationList.as_view()),
    path('accommodation/<int:pk>/', views.TripAccommodationDetail.as_view()),

    path('cost/', views.CostItemList.as_view()),
    path('cost/<int:pk>/', views.CostItemDetail.as_view()),

    path('accept_relationship/<int:pk>/', views.accept_relationship),
    path('accept_trip/<int:pk>/', views.accept_trip),
    path('approve_trip/<int:pk>/', views.approve_trip),
]
