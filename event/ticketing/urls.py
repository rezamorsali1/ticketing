from django.urls import path

from ticketing import views

app_name="ticketing"


urlpatterns = [
  
     
    path('event-list/',views.eventListView, name="event-list") ,
    path('location-list/',views.locationListView , name='location-list') ,
    path('event-details/<int:event_id>',views.eventDetailsView , name='event-details') ,
    path('time-list/',views.timeListView , name='time-list'),
    path('event-edit/<int:event_id>',views.eventEditView , name='event-edit') ,
    path('event-selection/',views.eventSelectionView , name='event-selection') ,
    path('event-list-selection/',views.eventListSelectionView , name='event-list-selection') ,
    path('export-CSV/', views.exportCSV, name='export-CSV'),

   

]