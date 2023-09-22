from django.shortcuts import render
from django.views.generic import TemplateView
#from .models import Appointments

# Create your views here.
def index(request):
    # if request.method == 'POST': 
    #     obj=Appointments()
    #     obj.patient_name=request.POST.get('patient_name')
    #     obj.doctor_name_name=request.POST.get('doctor')
    
    return render(request,'resources/index.html')
def news(request):
    return render(request,'resources/news.html')
def services(request):
    return render(request,'resources/services.html')
def gallery(request):
    return render(request,'resources/gallery.html')
def contact(request):
    return render(request,'resources/contact.html')



    
