from django.urls import path
from . import views

# urls for each view from views.py

# (url, views.py function, name)
urlpatterns = [
path("<str:name>", views.index, name="index"),
]
