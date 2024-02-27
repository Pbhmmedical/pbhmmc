from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.views.static import serve
from . import views

urlpatterns = [
    # ... your existing patterns ...

    path('robots.txt', views.robots_txt, name='robots_txt'),
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('booking', views.booking, name='booking'),
    path('doctors', views.doctors, name='doctors'),
    path('contact', views.contact, name='contact'),
    path('images', views.images, name='images'),
    path('department', views.department, name='department'),
    path('Gynechology', views.Gynechology, name='Gynechology'),
    path('Dental', views.Dental, name='Dental'),
    path('General', views.General, name='General'),
    path('doctor-details/<int:doctor_id>/', views.doctor_details, name='doctor-details'),
    path('service', views.service, name='service'),
    path('insurance', views.insurance, name='insurance'),
    path('notify_admin', views.notify_admin, name='notify_admin'),
    path('info', views.info, name='info')
]

