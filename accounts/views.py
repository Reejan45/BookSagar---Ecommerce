from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.views.generic import CreateView
from products.views import *



class UserRegistrationView(CreateView):
    form_class = UserCreationForm
    template_name = 'products/user_registration.html'

    def get_success_url(self):
        return reverse('store')
    
