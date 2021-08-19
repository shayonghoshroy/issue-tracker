from django.urls import path
from . import views

# urls for each view from views.py

# (url, views.py function, name)
urlpatterns = [
path("", views.home, name="home"),
path("create/", views.create, name="create"),
path("view/", views.view, name="view"),
path("project/", views.project, name="project"),
path("project/<int:id>/", views.project_index, name="project_index"),
path("project/<int:id>/issue/", views.issue, name="issue"),
path("project/<int:id>/issue/<int:issue_id>/", views.issue_index, name="issue_index"),
path("project/list/", views.project_list, name="project_list")
]
