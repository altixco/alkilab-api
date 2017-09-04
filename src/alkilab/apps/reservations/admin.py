from django.contrib import admin
from .models import Person, ReservationState, Country, \
                    State, City, RoomType, \
                    RoomState, Room, Reservation, \
                    Rental

class PersonAdmin(admin.ModelAdmin):
    pass
class ReservationStateAdmin(admin.ModelAdmin):
    pass
class CountryAdmin(admin.ModelAdmin):
    pass
class StateAdmin(admin.ModelAdmin):
    pass
class CityAdmin(admin.ModelAdmin):
    pass
class RoomTypeAdmin(admin.ModelAdmin):
    pass
class RoomStateAdmin(admin.ModelAdmin):
    pass
class RoomAdmin(admin.ModelAdmin):
    pass
class ReservationAdmin(admin.ModelAdmin):
    pass
class RentalAdmin(admin.ModelAdmin):
    pass

admin.site.register(Person, PersonAdmin)
admin.site.register(ReservationState, ReservationStateAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(RoomType, RoomTypeAdmin)
admin.site.register(RoomState, RoomStateAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Rental, RentalAdmin)