from django.db import models


# Create your models here.

class Departments(models.Model):
    dep_name = models.CharField(max_length=100)
    dep_description = models.TextField()
    dep_image = models.ImageField(upload_to='departments',)
    read_more_link = models.CharField(max_length=255, default='some_default_value')

    def __str__(self):
        return self.dep_name


class Doctors(models.Model):
    doc_name = models.CharField(max_length=255)
    doc_spec = models.CharField(max_length=255)
    doc_exp = models.TextField()
    doc_id = models.CharField(max_length=255, default='30')
    dep_name = models.ForeignKey(Departments, on_delete=models.CASCADE)
    doc_image = models.ImageField(upload_to='doctors')
    monday_hours = models.CharField(max_length=100, blank=True, null=True)
    tuesday_hours = models.CharField(max_length=100, blank=True, null=True)
    wednesday_hours = models.CharField(max_length=100, blank=True, null=True)
    thursday_hours = models.CharField(max_length=100, blank=True, null=True)
    friday_hours = models.CharField(max_length=100, blank=True, null=True)
    saturday_hours = models.CharField(max_length=100, blank=True, null=True)
    sunday_hours = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return 'Dr ' + self.doc_name + ' - (' + self.doc_spec + ')'





class Booking(models.Model):
    p_name = models.CharField(max_length=255)
    p_phone = models.CharField(max_length=10)
    p_email = models.EmailField()
    doc_name = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    booking_date = models.DateField()
    booked_on = models.DateField(auto_now=True)
    posted_status = models.BooleanField(default=False)
    booking_time = models.TimeField(null=True, blank=True)


class Images(models.Model):
    image_name = models.CharField(max_length=255)
    image_title = models.CharField(max_length=255)
    pic_image = models.ImageField(upload_to='gallery')

    def __str__(self):
        return self.image_name




class Insurance(models.Model):
    ins_comp=models.CharField(max_length=255)
    com_image = models.ImageField(upload_to='insurance')

    def __str__(self):
        return self.ins_comp


class Service(models.Model):
    dep_name = models.ForeignKey(Departments, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    icon_class = models.CharField(max_length=50)
    description = models.TextField()
    read_more_link = models.CharField(max_length=255)

    def __str__(self):
        return self.title

