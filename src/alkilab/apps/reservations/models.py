from django.db import models
from django.contrib.auth.models import User




class Person(models.Model):
    """Model definition for Person."""
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    birth_date = models.DateField(auto_now=False, auto_now_add=False)
    id_number = models.IntegerField(blank=False)

    user = models.ForeignKey(User)

    def __str__(self):
        return self.firstname

class ReservationState(models.Model):
    """Model definition for the reservation's states."""
    name = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.name

class Country(models.Model):
    """Model definition for Country."""
    name = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.name

class State(models.Model):
    """Model definition for State."""
    name = models.CharField(max_length=50, blank=False)

    country = models.ForeignKey(Country)

    def __str__(self):
        return self.name

class City(models.Model):
    """Model definition for City."""
    name = models.CharField(max_length=50, blank=False)

    state = models.ForeignKey(State)

    class Meta:
        verbose_name_plural = 'Cities'
    
    def __str__(self):
        return self.name

class RoomType(models.Model):
    """Model definition for the room's type."""
    name = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.name

class RoomState(models.Model):
    """Model definition for room's state."""
    name = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.name
    
class Room(models.Model):
    """Model definition for Room."""
    name = models.CharField(max_length=50, blank=False)
    address = models.CharField(max_length=100, blank=True)
    capacity = models.IntegerField(default=1, blank=False)
    enabled = models.BooleanField(default=True)
    use_counter = models.IntegerField(default=0)

    city = models.ForeignKey(City, null=True)
    room_state = models.ForeignKey(RoomState, null=True)
    room_type = models.ForeignKey(RoomType, null=True)
    
    def __str__(self):
        return self.name

class Reservation(models.Model):
    """Model definition for Reservation."""
    date = models.DateField(auto_now=False, 
                            auto_now_add=False, 
                            blank=False)

    start_hour = models.DateTimeField(
                            auto_now=False, 
                            auto_now_add=False,
                            blank=False)

    end_hour = models.DateTimeField(auto_now=False, 
                                    auto_now_add=False,
                                    blank=False)

    purpose = models.TextField()
    
    est_attendance = models.IntegerField(default=1)

    person = models.ForeignKey(Person)
    room = models.ForeignKey(Room)
    state = models.ForeignKey(ReservationState)

    def __str__(self):
        return "Room: %s is reserved at %s" % (self.room.name, self.start_hour)

class Rental(models.Model):
    """Model definition for Rentals."""
    attendance = models.IntegerField()

    reservation = models.ForeignKey(Reservation)

    def __str__(self):
        return "Rentals for the reservation: %s" % self.reservation