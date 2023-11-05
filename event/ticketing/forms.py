from django import forms
from ticketing.models import EventModel

class SearchForm(forms.Form):
    searchText= forms.CharField(max_length=100 ,label="Event" ,required=False )


class EventForm(forms.ModelForm):
    class Meta:
        model = EventModel 
        fields=['name','teacherName','lenght' ,'poster']
        # exclude =['poster']


