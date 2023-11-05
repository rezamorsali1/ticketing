from django.contrib import admin
from ticketing.models import EventModel
from ticketing.models import LocationModel
from ticketing.models import TimeModel
# from ticketing.models import ProfileModel
from ticketing.models import TicketModl




# Register your models here.
admin.site.register(EventModel)
admin.site.register(LocationModel)
admin.site.register(TimeModel)
# admin.site.register(ProfileModel)
admin.site.register(TicketModl)


