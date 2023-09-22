from django.test import TestCase
from apps.resources import models

class TestModel(TestCase):
    def setUp(self):
        self.dept_name ='Cardiology'
        self.dept=models.Departments(name=self.dept_name)
        
    def test_create_object(self):
        self.assertInstance(self.dept, models.Departments)        
        
    