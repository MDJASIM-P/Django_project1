"""company URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Root url file of project 
from django.contrib import admin
from django.urls import path, include
from employee import views
from accounts import views as acc_views


urlpatterns = [
    path('admin/', admin.site.urls),
    # from employee app
    path('first/',views.firstrequest),
    path('second/',views.secondrequest),
    path('employee/',views.home),
    path('employee/details/', views.empdetials),

    path('login/',acc_views.login),
    path('data/',acc_views.data),
    path('accounts/signup/', acc_views.signup),
    # created 
    # path('', include('accounts.urls_acc')), # import accounts.urls_acc

]




