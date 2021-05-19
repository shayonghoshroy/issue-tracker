from django.urls import path
from . import views

# urls for each view from views.py

# (url, views.py function, name)
urlpatterns = [
path("", views.home, name="home"),
path("create/", views.create, name="create"),
path("<int:id>", views.project_index, name="project_index"),
path("view/", views.view, name="view"),
path("project", views.project, name="project")
]
