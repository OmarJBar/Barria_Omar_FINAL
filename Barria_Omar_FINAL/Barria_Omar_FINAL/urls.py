"""
URL configuration for Proyecto_8 project.

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
from barria_mobile_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('inscrito_list/', views.inscrito_list),
    path('inscrito_detalle/<int:id>', views.inscrito_detalle),
    path('inscrito_class', views.inscrito_list_class.as_view())
]
