from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path(route='hello/', view=views.say_hello)
]