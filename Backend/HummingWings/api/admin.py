from django.contrib import admin
from api.models.email_template import EmailTemplate
from api.models.email_tracking import EmailTracking
from api.models.environment_variables import EnvironmentVariables
from api.models.root import Root
from api.models.user import User
from api.models.ticket import Ticket
from api.models.booking_holder import BookingHolder
from api.models.flight import Flight
from api.models.seat import Seat
from api.models.card import Card
from api.models.new import New
from api.models.passenger import Passenger
from api.models.search_log import SearchLog


# Register your models here.
admin.site.register(Root)
admin.site.register(User)
admin.site.register(EmailTemplate)
admin.site.register(EmailTracking)
admin.site.register(EnvironmentVariables)
admin.site.register(Ticket)
admin.site.register(BookingHolder)
admin.site.register(Flight)
admin.site.register(Seat)
admin.site.register(Card)
admin.site.register(New)
admin.site.register(Passenger)
admin.site.register(SearchLog)
