"""
URL configuration for clinicalservices project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from clinicalapp import views
from rest_framework import routers
from django.conf.urls import include



router =routers.DefaultRouter()
router.register(r'patients',views.PatientViewSet)
router.register(r'clinicaldata',views.ClinicalDataViewSet)  


urlpatterns = [
    path('admin/', admin.site.urls),
    path('clinicalservices/api/', include(router.urls)),

]
