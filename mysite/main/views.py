from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . models import ToDoList, Item
from . forms import CreateNewList

# Create your views here.

def index(response, id):
    if not response.user.is_authenticated:
        return HttpResponseRedirect("/login/")

    ls = ToDoList.objects.get(id=id)
    if ls in response.user.todolist.all():
        if response.method == "POST":
            print(response.POST)
            if response.POST.get("save"):  # was the save button pressed ?
                for item in ls.item_set.all():
                    if response.POST.get("c" + str(item.id)) == "clicked":
                        item.complete = True
                    else:
                        item.complete = False
                    item.save()
            elif response.POST.get("newItem"):
                txt = response.POST.get("new")
                if len(txt) > 2:
                    # TODO: add input validation
                    ls.item_set.create(text=txt, complete=False)
                else:
                    print("invalid")
        return render(response, "main/list.html", {"ls":ls})
    else:
        return render(response, "main/view.html", {})


    #item = ls.item_set.all().get(id=1)
    #return HttpResponse("<h1>%s</h1><br></br><p>%s</p>" % (ls, item))

def home(response):
    if not response.user.is_authenticated:
        return HttpResponseRedirect("/login/")

    return render(response, "main/home.html", {})

# user creates todo list
def create(response):
    if not response.user.is_authenticated:
        return HttpResponseRedirect("/login/")

    if response.method == "POST":
        # response.POST is a dict of input attributes
        form = CreateNewList(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"] # access a value from key
            t = ToDoList(name=n)
            t.save()
            response.user.todolist.add(t) # save todolist to specific user

            #t = ToDoList(name=n)
            #t.save()

        return HttpResponseRedirect("/%i" %t.id)
    else:
        form = CreateNewList()
    return render(response, "main/create.html", {"form":form})

def project(response):
    if not response.user.is_authenticated:
        return HttpResponseRedirect("/login/")

    if response.method == "POST":
        form = CreateNewList(response.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            d = form.cleaned_data["description"]
            p = Project(name=n, description=d)
            p.save()
            response.user.project.add(p)
        return HttpResponseRedirect("/") # TODO: redirect to project view
    else:
        form = CreateNewList()
    return render(response, "main/project.html", {"form":form})

def view(response):
    if not response.user.is_authenticated:
        return HttpResponseRedirect("/login/")
    return render(response, "main/view.html", {})
