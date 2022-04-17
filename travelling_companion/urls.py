from django.contrib.auth.decorators import login_required
from django.urls import path, include
from django.views.generic import TemplateView

from travelling_companion import views

app_name = 'travelling_companion'
urlpatterns = [
    path('', views.TripListView.as_view(), name='home'),

    path('trip/<int:pk>', views.TripDetailView.as_view(), name='trip_detail'),
    path('trip/delete/<int:pk>', views.TripDeleteView.as_view(), name='trip_delete'),
    path('trip/create', views.TripCreateView.as_view(), name='trip_create'),
    path('trip/update/<int:pk>', views.TripUpdateView.as_view(), name='trip_update'),

    path('trip/<int:trip_id>/cost', views.CostView.as_view(), name='cost_form'),
    path('trip/<int:trip_id>/cost/<int:pk>', views.CostEditView.as_view(), name='cost_edit_form'),
    path('trip/cost/delete/<int:pk>', views.CostDelete.as_view(), name='cost_delete'),

    path('trip/<int:trip_id>/flight', views.FlightView.as_view(), name='flight_form'),
    path('trip/<int:trip_id>/flight/<int:pk>', views.FlightEditView.as_view(), name='flight_edit_form'),
    path('trip/flight/delete/<int:pk>', views.FlightDelete.as_view(), name='flight_delete'),

    path('trip/<int:trip_id>/accommodation', views.AccommodationView.as_view(), name='accommodation_form'),
    path('trip/<int:trip_id>/accommodation/<int:pk>', views.AccommodationEditView.as_view(), name='accommodation_edit'),
    path('trip/accommodation/delete/<int:pk>', views.AccommodationDelete.as_view(), name='accommodation_delete'),

    path('trip/accept/<int:pk>', views.AccepteTrip.as_view(), name='trip_accept'),
    path('trip/approve/<int:pk>', views.ApproveTrip.as_view(), name='trip_approve'),
    path('trip/<int:pk>/add_person/<int:person_id>', views.AddPersonTrip.as_view(), name='trip_add_person'),
    path('trip/remove_person/<int:pk>', views.RemovePersonTrip.as_view(), name='trip_remove_person'),

    path('location/', views.LocationView.as_view(), name='location_form'),
    path('location/<int:pk>', views.LocationEditView.as_view(), name='location_edit_form'),
    path('location/delete/<int:pk>', views.LocationDelete.as_view(), name='location_delete'),

    path('person/', views.PersonListView.as_view(), name='person_list'),
    path('person/delete/<int:pk>', views.PersonDeleteView.as_view(), name='person_delete'),
    path('person/create', views.PersonCreateView.as_view(), name='person_create'),
    path('person/update/<int:pk>', views.PersonUpdateView.as_view(), name='person_update'),

    path('passport/create', views.PassportCreateView.as_view(), name='passport_create'),

]
