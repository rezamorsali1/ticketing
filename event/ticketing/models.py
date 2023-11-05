from django.db import models
from accounts.models import ProfileModel


# Create your models here.

class EventModel(models.Model):
    name = models.CharField(max_length= 50)
    teacherName = models.CharField(max_length=50)
    lenght =models.IntegerField()
    poster = models.ImageField(upload_to='eventImages/', null=True)

    def __str__(self):
        return self.name


class LocationModel(models.Model):
    name = models.CharField(max_length= 50)
    address=models.CharField(max_length= 150,default="karaj-milad")
    phone=models.CharField(max_length= 11)

    def __str__(self):
        return self.name
    

class TimeModel(models.Model):
    eventModel = models.ForeignKey("EventModel", on_delete=models.PROTECT)
    locationModel = models.ForeignKey("LocationModel", on_delete=models.PROTECT)
    startDateTime = models.DateTimeField()
    seats = models.IntegerField()
    start=1
    end=2
    cancel=3
    sales =4

    startus_choice =((start,"Starting"),(end, "SoldOut"),(cancel ,"Canceld"),(sales,"saling"))
    status = models.IntegerField(choices= startus_choice)

    def __str__(self) :

        return f"Time:{self.startDateTime} Event:{self.eventModel} Location:{self.locationModel}"
    


 
 

    
class TicketModl(models.Model):
    name = models.CharField(max_length=50)
    price= models.IntegerField()
    timeModel = models.ForeignKey("TimeModel", on_delete=models.PROTECT)
    profileModel = models.ForeignKey(ProfileModel, on_delete=models.PROTECT)
    TicketImage = models.ImageField(upload_to='ticketImages/', null=True)

    
    def __str__(self) :

        return f"Ticket Info: Profile{self.profileModel} Time:{self.timeModel}"


























