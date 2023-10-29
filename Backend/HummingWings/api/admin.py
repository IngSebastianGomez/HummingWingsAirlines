from django.contrib import admin
from api.models.email_template import EmailTemplate
from api.models.email_tracking import EmailTracking
from api.models.environment_variables import EnvironmentVariables
from api.models.root import Root
from api.models.user import User
from api.models.ticket import Ticket
from api.models.booking_holder import BookingHolder
from api.models.flights import Flights
from api.models.seat import Seat
from api.models.cards import Cards
from api.models.news import News
from api.models.passenger import Passenger



# Register your models here.
admin.site.register(Root)
admin.site.register(User)
admin.site.register(EmailTemplate)
admin.site.register(EmailTracking)
admin.site.register(EnvironmentVariables)
admin.site.register(Ticket)
admin.site.register(BookingHolder)
admin.site.register(Flights)
admin.site.register(Seat)
admin.site.register(Cards)
admin.site.register(News)
admin.site.register(Passenger)



