from django.shortcuts import render
from django.http import HttpResponse
from . models import ToDoList, Item

# Create your views here.

def index(response, name):
    ls = ToDoList.objects.get(name=name)
    return render(response, "main/list.html", {"ls":ls})
    #item = ls.item_set.all().get(id=1)
    #return HttpResponse("<h1>%s</h1><br></br><p>%s</p>" % (ls, item))

def home(response):
    return render(response, "main/home.html", {})

# user creates todo list
def create(response):
    return render(response, "main/create.html", {})
