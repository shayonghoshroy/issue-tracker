from django.shortcuts import render
from django.http import HttpResponse
from . models import ToDoList, Item
from . forms import CreateNewList

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
    if response.method == "POST":
        # response.POST is a dict of input attributes
        form = CreateNewList(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"] # access a value from key
            t = ToDoList(name=n)
            t.save()
    else:
        form = CreateNewList()
    return render(response, "main/create.html", {"form":form})
