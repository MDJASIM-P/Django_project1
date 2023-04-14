from django.urls import path
from .views import *     # * for complete functions from views.py

urlpatterns = [
    path('', home),

    path('', home, name='hm'), # path of 'Home page' link 
    path('login', login, name="lg"), # url name, path of 'Login' on home page
    path('signup', signup, name="su") # path of 'Signup' on home page
]


