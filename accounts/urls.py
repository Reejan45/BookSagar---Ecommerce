from django.urls import path,include
from . import views
from . views import *
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView

app_name= 'accounts'

urlpatterns = [
   path('new-user', UserRegistrationView.as_view(), name='user_registration'),
   path('login', LoginView.as_view(template_name='products/login.html'), name="login"),
   path('logout', LogoutView.as_view(template_name='products/login.html'), name="logout"),
   path('products',include('products.urls')),
]