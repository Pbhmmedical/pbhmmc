from ast import Return
from enum import Flag
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import BookingForm
from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail



from .models import Departments, Doctors,Images,Service
from .models import Insurance



from .models import Doctors, Departments  # Import your Departments model at the top

from django.shortcuts import render
from .models import Doctors, Departments, Booking
from .forms import BookingForm  # Import your BookingForm

from .models import Insurance  # Import the Insurance model if not already imported




def send_admin_notification(appointment_details):
    subject = 'New Appointment Booking'
    message = f'A new appointment has been booked. Details: {appointment_details}'
    from_email = 'shamsadparayil@gmail.com'
    recipient_list = ['shamsad1993@yahoo.com']

    send_mail(subject, message, from_email, recipient_list)



def index(request):
    doctors = Doctors.objects.all().order_by('doc_id')
    departments = Departments.objects.all()
    insurances = Insurance.objects.all()
    services = Service.objects.all()  # Fetch all Service objects

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            # Modify the booking_time data to match the format
            form.cleaned_data['booking_time'] = form.cleaned_data['booking_time'].strftime('%I:%M %p')
            form.save()  # Save the form data to the database

            # Use 'booking_date' and 'booking_time' to access the booking date and time fields
            appointment_details = f'Date: {form.cleaned_data["booking_date"]}, Time: {form.cleaned_data["booking_time"]}, Patient Name: {form.cleaned_data["p_name"]}, Mobile Number: {form.cleaned_data["p_phone"]}, Patient Email: {form.cleaned_data["p_email"]}, Doctor Name: {form.cleaned_data["doc_name"]}'

            # Send email notification to the admin
            send_admin_notification(appointment_details)

            return render(request, 'confirmation.html')
    else:
        form = BookingForm()

    context = {
        'form': form,
        'doctors': doctors,
        'departments': departments,
        'insurances': insurances,
        'services': services,  # Add services to the context
    }

    return render(request, 'index.html', context)






def about(request):
    return render(request, 'about.html')

def Gynechology(request):
    try:
        # Assuming the gynecology department has a specific name, e.g., 'Gynechology'
        department = Departments.objects.get(dep_name='GYNECOLOGY')
        doctors = Doctors.objects.filter(dep_name=department)
    except Departments.DoesNotExist:
        department = None
        doctors = None

    context = {
        'department': department,
        'doctors': doctors,
    }

    return render(request, 'Gynechology.html', context)


def Dental(request):
    try:
        # Assuming the dental department has a specific name, e.g., 'Dental'
        department = Departments.objects.get(dep_name='DENTAL')
        doctors = Doctors.objects.filter(dep_name=department)
    except Departments.DoesNotExist:
        department = None
        doctors = None

    context = {
        'department': department,
        'doctors': doctors,
    }

    return render(request, 'Dental.html', context)

def General(request):
    return render(request, 'General.html')




def doctors(request):
    dict_docs = {
        'doctors': Doctors.objects.all().order_by('doc_id')
    }
    return render(request, 'doctors.html', dict_docs)



def contact(request):
    # Retrieve existing bookings
    bookings = Booking.objects.all()

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            # Create a new Booking instance, modify if needed, and save
            booking_instance = form.save(commit=False)
            # Additional processing if necessary
            booking_instance.save()
            # Redirect to a confirmation page
            return render(request, 'confirmation.html')
    else:
        form = BookingForm()

    # Retrieve insurance data
    insurances = Insurance.objects.all()

    context = {
        'form': form,            # Include the form in the context
        'bookings': bookings,    # Include existing bookings
        'insurances': insurances,  # Include insurance data in the context
        # Add other relevant data to the context as needed
    }

    return render(request, 'contact.html', context)


def service(request):
    departments = Departments.objects.all()
    services = Service.objects.all()  # Fetch all services from the database

    context = {
        'departments': departments,
        'services': services,  # Add services to the context
    }

    return render(request, 'service.html', context)

def department(request):
    dict_dept = {
        'dept': Departments.objects.all()
    }
    return render(request, 'department.html', dict_dept)


def images(request):
    dict_images = {
        'images': Images.objects.all()
    }
    return render(request, 'images.html', dict_images)





def doctor_detail(request, doctor_id):
    doctor = get_object_or_404(Doctors, id=doctor_id)
    return render(request, 'doctor_detail.html', {'doctor': doctor})

def insurance(request):
    dict_insurance = {
        'insurance': Insurance.objects.all()
    }
    return render(request, 'insurance.html', dict_insurance)

def doctor_details(request, doctor_id):
    # Retrieve the doctor object based on the provided doctor_id
    doctor = Doctors.objects.get(id=doctor_id)

    context = {
        'doctor': doctor,
    }

    return render(request, 'doctor_details.html', context)

def notify_admin(request):
    # Replace with the actual admin email address
    admin_email = 'shamsadparayil@gmail.com'
    subject = 'New Appointment Booking'
    message = 'A new appointment has been booked. Check the admin dashboard for details.'

    send_mail(subject, message, 'shamsadparayil@gmail.com', [admin_email])

    return render(request, 'notification_sent.html')

def robots_txt(request):
    content = "User-agent: *\nDisallow: /private/\nDisallow: /secret/"
    return HttpResponse(content, content_type="text/plain")

def info(request):
    bookings = Booking.objects.all()

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return render(request, 'confirmation.html')
    else:
        form = BookingForm()
    return render(request, 'info.html')

# views.py or wherever you handle appointment bookings






def send_admin_notification(appointment_details):
    subject = 'New Appointment Booking'
    message = f'A new appointment has been booked. Details: {appointment_details}'
    from_email = 'shamsadparayil@gmail.com'  # your email
    recipient_list = ['shamsad1993@yahoo.com']  # your email or the email where you want to receive notifications

    send_mail(subject, message, from_email, recipient_list)

def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            # Check if booking_time is not None before formatting
            booking_time = form.cleaned_data['booking_time']
            if booking_time:
                form.cleaned_data['booking_time'] = booking_time.strftime('%I:%M %p')

            form.save()

            appointment_details = f'Date: {form.cleaned_data["booking_date"]}, Time: {form.cleaned_data["booking_time"]}, Patient Name: {form.cleaned_data["p_name"]}, Mobile Number: {form.cleaned_data["p_phone"]}, Patient Email: {form.cleaned_data["p_email"]}, Doctor Name: {form.cleaned_data["doc_name"]}'

            send_admin_notification(appointment_details)

            return render(request, 'confirmation.html')
    else:
        form = BookingForm()

    dict_form = {
        'form': form
    }

    return render(request, 'booking.html', dict_form)



