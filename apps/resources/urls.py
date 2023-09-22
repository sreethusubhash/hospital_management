from django.urls import path
from. import views

urlpatterns = [
    path('', views.index),
    path('home/',views.index),
    path('news/', views.news),
    path('services/', views.services),
    path('gallery/', views.gallery),
    path('contact/', views.contact),
]