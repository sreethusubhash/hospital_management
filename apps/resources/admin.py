from django.contrib import admin
from apps.resources import models
#from apps.resources.models import Departments
# Register your models here.

class ResourcesDetails(admin.ModelAdmin):
    list_display=(
        'dept_name',
        'get_description'
    )

    @admin.display(description='descriptions')
    def get_description(self,obj):
        if len(obj.descriptions)>50 :
            return f'{obj.descriptions[:50]}...'
        else:
            return obj.descriptions
              
admin.site.register(models.Departments)
admin.site.register(models.Resources,ResourcesDetails)
admin.site.register(models.Doctors)
admin.site.register(models.Appointments)

