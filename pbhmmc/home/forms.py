from django import forms
from .models import Booking

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'

        widgets = {
            'booking_date': DateInput(),
            'booking_time': TimeInput(),
        }

        labels = {
            'p_name': 'Patient Name',
            'p_phone': 'Phone Number',
            'p_email': 'Email',
            'dep_name': 'Department Name',
            'doc_name': 'Doctor Name',
            'booking_date': 'Booking Date',
            'booking_time': 'Booking Time',
        }
