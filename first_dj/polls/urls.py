from django.urls import path

from . import views
from . import little_thing

urlpatterns = [
    path('', views.index, name='index')
]