from django.urls import path 
from . import views 


app_name = 'online_registration_form'

urlpatterns = [
    path("", views.register, name="register"),
]