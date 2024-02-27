from django.contrib import admin
from .models import Departments, Doctors, Booking, Images, Insurance , Service


admin.site.register(Departments)
admin.site.register(Doctors)
admin.site.register(Images)
admin.site.register(Insurance)
admin.site.register(Service)


class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'p_name', 'p_phone', 'p_email', 'doc_name', 'booking_date', 'booking_time_display', 'booked_on', 'posted_status')

    def booking_time_display(self, obj):
        return obj.booking_time  # Assuming booking_time is a field on the Booking model

    booking_time_display.short_description = 'Booking Time'




admin.site.register(Booking, BookingAdmin)