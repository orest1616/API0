"""API URL Configuration

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
from django.contrib import admin
from django.urls import path

from VPO.views import VpoAPIView
from VPO.views import Register_organizer
from VPO.views import Register_member
from VPO.views import Project
from VPO.views import Sing

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/name/', VpoAPIView.as_view()),
    path('api/v1/register_organizer/', Register_organizer.as_view()),
    path('api/v1/register_member/', Register_member.as_view()),
    path('api/v1/organizer_project/', Project.as_view()),
    path('api/v1/sing/', Sing.as_view())
]
