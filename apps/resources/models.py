from django.db import models
from apps.core.models import CreatedModifiedDateTimeBase
from apps.user.models import User

# Create your models here.
class Departments(CreatedModifiedDateTimeBase):
    #dept_id=models.IntegerField()
    dept_name = models.CharField(max_length=100)
    def __str__(self):
        return self.dept_name
    class Meta:
        verbose_name_plural = "Departments"
class Resources(CreatedModifiedDateTimeBase):
    user_id = models.ForeignKey("user.User", null=True, on_delete=models.SET_NULL)
    dept_name= models.ForeignKey("resources.Departments",default = 1, on_delete=models.SET_DEFAULT)
    #dept_name = models.CharField(max_length=100)
    descriptions = models.TextField(max_length=1000)
    class Meta:
        verbose_name_plural = "Resources"
    def get_description(self):
        return self.descriptions[:50]

    def __str__(self):
    	return f'{self.user_id.username}: {self.dept_name}'
    
class Doctors(CreatedModifiedDateTimeBase):
    doctor_name = models.CharField(max_length=100)
    doctor_specialization = models.TextField(max_length=1000)
    dept_name = models.ForeignKey(Departments, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = "Doctors"
    def __str__(self):
    	return f'Dr:{self.doctor_name}: {self.dept_name}'
 
 
class Appointments(CreatedModifiedDateTimeBase):
    doctor_name = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=100)
    patient_email=models.EmailField(max_length=50)
    patient_phone=models.CharField(max_length=50)
    #appointment_date=models.DateField()
    class Meta:
        verbose_name_plural = "Appointments"
    def __str__(self):
        return f'{self.doctor_name}'
    
    def __str__(self):
    	return f'{self.doctor_name}: {self.patient_name}'
    
    