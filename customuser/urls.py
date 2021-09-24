

from django.urls import path
from . import views
# Create your models here.
urlpatterns = [
    path("", views.home, name="home"),
]