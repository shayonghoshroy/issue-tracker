from django.contrib import admin
from . models import ToDoList, Item, Project, Issue

# Register your models here.

admin.site.register(ToDoList)
admin.site.register(Item)
admin.site.register(Project)
admin.site.register(Issue)
