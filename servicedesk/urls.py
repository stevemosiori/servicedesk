"""servicedesk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import include, path
from django.contrib.auth import views as auth_views
from sdapp.views import (
    index,
    dashboard, 
    profile, 
    settings, 
    tickets, 
    new_ticket,
    upload_attachment,
)

urlpatterns = [
    path('', index, name='index'),
    path('settings/', settings, name='settings'),
    path('tickets/', tickets, name='tickets'),
    path('tickets/new/', new_ticket, name='tickets.new'),
    path('tickets/attachments/upload', upload_attachment, name='tickets.attachment.upload'),
    path('dashboard/', dashboard, name='dashboard'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]
