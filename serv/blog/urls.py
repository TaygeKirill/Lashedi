from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='general'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('jobs', views.jobs, name='jobs'),
    path('calendar', views.calendar, name='calendar'),
    path('price', views.price, name='price'),
]