from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from ticketing.models import LocationModel
from ticketing.models import EventModel , LocationModel ,TimeModel
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from ticketing.forms import SearchForm , EventForm
import datetime , csv


def homeView(request):
     return HttpResponse("Welcome")


def eventListView(request) :
     searchForm = SearchForm(request.GET)
     if(searchForm.is_valid()):
          searchText=searchForm.cleaned_data["searchText"]
          eventList = EventModel.objects.filter(name__contains=searchText)
           
           
     else:
          eventList = EventModel.objects.all()
          
   
     context={
          "eventList":eventList ,
          "eventCount":eventList.count() ,
          "searchForm":searchForm

          
     }

     return render(request,'ticketing/event-list.html',context)

 #==========================1
@login_required
def locationListView(request) :
    
     locationList = LocationModel.objects.all()

   
     context={
          "locationList":locationList ,
          
          
     }

     return render(request,'ticketing/location-list.html',context)


 #==========================
@login_required
def eventDetailsView(request, event_id) :
    
     eventdetails = EventModel.objects.get(pk=event_id)

   
     context={
          "eventdetails":eventdetails ,
          
          
     }

     return render(request,'ticketing/event-details.html',context)


 #==========================1
@login_required
def timeListView(request) :

#     if request.user.is_authenticated and request.user.is_active:
          timeList = TimeModel.objects.all()
          context={
               "timeList":timeList ,
   
          }
          return render(request,'ticketing/time-list.html',context)
    
          
#     else:
#           return HttpResponseRedirect(reverse("accounts:login"))
     #     return HttpResponse("Pls Login...")


def eventEditView(request ,event_id ):
     eventdetails = EventModel.objects.get(pk=event_id)
     if request.method =="POST":
          eventForm =EventForm(request.POST ,request.FILES,instance=eventdetails)
          if eventForm.is_valid():
               eventForm.save()
               return HttpResponseRedirect(reverse("ticketing:event-list"))
     else:
           eventForm =EventForm(instance=eventdetails)
           
                
    
     context ={
           "eventForm":eventForm ,
           "posterImage":eventdetails.poster

     }
     return render(request,'ticketing/event-edit.html',context)


#===================================
def eventSelectionView(request):
     events= EventModel.objects.all()
     context={
           "events":events
     }
     return render(request,'ticketing/event-selection.html',context)


#==============================
def eventListSelectionView(request):
     if  request.method =="POST" :
          selected_event_ids = request.POST.getlist('selected_events')
          request.session['selected_event_ids'] =selected_event_ids 

          print (selected_event_ids )
          selected_events =EventModel.objects.filter(id__in=selected_event_ids )
          print(selected_events)

          context={
               "events":selected_events ,

          }
          return render(request,'ticketing/event-list-selection.html',context)

#==============================
def exportCSV(request):
    selected_event_ids = request.session.get('selected_event_ids', [])
    selected_events = EventModel.objects.filter(id__in=selected_event_ids)
    

    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename=selectedEvents' + str(datetime.datetime.now()) + '.csv'

    
#     response["Content-Disposition"] = 'attachment; filename=selectedEvents.csv'
    writer = csv.writer(response)
    writer.writerow(['id', 'name', 'teacherName'])
    
    for event in selected_events:
        writer.writerow([event.id, event.name, event.teacherName])
    
    return response


#==============================




   

       
      

      
      
     
      
      

    

    
         

     
         

         
    
  
         
         
         