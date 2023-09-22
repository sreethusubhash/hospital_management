from django.db import models
from apps.core.models import CreatedModifiedDateTimeBase
from apps.user.models import User

# Create your models here.


class Patients(CreatedModifiedDateTimeBase):
    name=models.CharField(max_length=100)
    contact_number=models.CharField(max_length=50)
    email=models.EmailField(max_length=100) 
class Hospital(CreatedModifiedDateTimeBase):
    pass
    
class Departments(CreatedModifiedDateTimeBase):
    
    dept_name = models.CharField(max_length=100)
    def __str__(self):
        return self.dept_name
    
    class Meta:
        verbose_name_plural = "Departments"
class Resources(CreatedModifiedDateTimeBase):
    user_id = models.ForeignKey("user.User", null=True, on_delete=models.SET_NULL)
    dept_name= models.ForeignKey("resources.Departments",default = 1, on_delete=models.SET_DEFAULT)
    descriptions = models.TextField(max_length=1000)
    class Meta:
        verbose_name_plural = "Resources"
    def get_description(self):
        return self.descriptions[:50]
    def __str__(self):
        return self.dept_id.dept_name

    # def __str__(self):
    # 	return f'{self.user_id.username}: {self.dept_name}'
  
class Doctors(CreatedModifiedDateTimeBase):
    doctor_name = models.CharField(max_length=100)
    doctor_specialization = models.TextField(max_length=1000)
    dept_name = models.ForeignKey(Departments, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = "Doctors"
    def __str__(self):
    	return f'{self.doctor_name}'
    def __str__(self):
    	return f'Dr:{self.doctor_name}: {self.dept_name}'
    def __str__(self):
    	return f'{self.doctor_name}'
 
class Appointments(CreatedModifiedDateTimeBase):
    doctor = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    patient= models.ForeignKey('resources.Patients', on_delete=models.SET_DEFAULT, default=None)
    appointment_date=models.DateField()
    appointment_time=models.TimeField()
   
    
    
    class Meta:
        verbose_name_plural = "Appointments"
    def __str__(self):
        return f'{self.doctor_name}'
   
    def __str(self):
    	return f"Appointment for {self.patient} with Dr. {self.doctor} on {self.appointment_date} at {self.appointment_time}"
    def __str__(self):
    	return f'{self.doctor_name}: {self.patient_name}'
    
    
