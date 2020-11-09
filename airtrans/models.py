from django.db import models


# Create your models here.

class Booking(models.Model):
    book_ref = models.AutoField(primary_key=True)
    book_date = models.DateField()
    total_amount = models.FloatField()


class Ticket(models.Model):
    ticket_no = models.AutoField(primary_key=True)
    book_ref = models.ForeignKey('Booking', on_delete=models.CASCADE)
    passenger_id = models.PositiveIntegerField()
    passenger_name = models.CharField(max_length=50)
    contact_data = models.EmailField(max_length=50)


class Flight(models.Model):
    flight_id = models.AutoField(primary_key=True)
    flight_no = models.CharField(max_length=10)
    arrival_airport = models.ForeignKey('Airport', on_delete=models.CASCADE, related_name='+')
    departure_airport = models.ForeignKey('Airport', on_delete=models.CASCADE, related_name='+')
    # departure_airport =
    # arrival_airport


class TicketFlight(models.Model):
    FARE_CONDITION = (
        ('1', 'Эконом класс'),
        ('2', 'Бизнес класс'),
        ('3', 'Первый класс')
    )
    ticket_no = models.ForeignKey('Ticket', on_delete=models.CASCADE)
    flight_id = models.ForeignKey('Flight', on_delete=models.CASCADE)
    fare_condition = models.CharField(max_length=1,
                                      choices=FARE_CONDITION
                                      )

    # amount =
    class Meta:
        unique_together = (('ticket_no', 'flight_id'),)


class Airport(models.Model):
    airport_code = models.CharField(max_length=3)


class BoardingPass(models.Model):
    ticket_no = models.OneToOneField('TicketFlight', on_delete=models.CASCADE)
    boarding_no = models.PositiveIntegerField()
    seat_no = models.CharField(max_length=3)

    # def clean(self):
    #     if self.seat_no[1]



    # class Meta:
    #     default_related_name = 'Boarding Pass'


# class BoardingPasses(models.Model):
#     ticket_no
#     flight_id
#     boarding_no
#     seat_no
