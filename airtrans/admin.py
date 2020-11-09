from django.contrib import admin
from .models import Booking, Ticket, Flight, TicketFlight, Airport, BoardingPass

# Register your models here.

admin.site.register(Booking)
admin.site.register(Ticket)
admin.site.register(Flight)
admin.site.register(TicketFlight)
admin.site.register(Airport)
admin.site.register(BoardingPass)
