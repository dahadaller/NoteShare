"""NoteShare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from . import views
from django.urls import include, path

urlpatterns = [
    path('', admin.site.urls, name='home'),
    path('register/',views.Register.as_view(),name='register' )
] 

# Admin Site Config
admin.sites.AdminSite.site_header = 'NoteShare Login'
admin.sites.AdminSite.site_title = 'NoteShare'
admin.sites.AdminSite.index_title = 'Welcome to NoteShare'
admin.sites.AdminSite.site_url = ""
