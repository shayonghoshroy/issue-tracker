from django.urls import path
from . import views

# urls for each view from views.py

# (url, views.py function, name)
urlpatterns = [
path("", views.index, name="index"),
path("v1/", views.v1, name="view 1"),
]
