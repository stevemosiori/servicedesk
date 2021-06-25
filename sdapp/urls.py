from django.conf.urls import url
from django.urls import include, path
from django.views.generic import RedirectView

from . import views

app_name = 'sdapp'
urlpatterns = [
    path('', views.Home.as_view(), name='index'),
]