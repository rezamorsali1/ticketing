from django.http import HttpResponse
from django.shortcuts import render
from ticketing.models import EventModel

# Create your views here.
# def eventListView(request) :
#      return HttpResponse("Event List")

# def eventListView(request) :
#      eventList = EventModel.objects.all()
#      return HttpResponse(eventList)

def eventListView(request) :
     eventList = EventModel.objects.all()
     text=f'''
        <!DOCTYPE html>
        <html >
        <head>
        
        </head>
        <body>
        <ul>
            {"".join(f'<li>{event}</li>'for event in  eventList)}
        </ul>
        </body>
        </html>


'''

     return HttpResponse(text)