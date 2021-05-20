from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . models import ToDoList, Item, Project, Issue
from . forms import CreateNewList
from django.contrib.auth import get_user_model
import json

# Create your views here.

# view project by id
def project_index(response, id):
    if not response.user.is_authenticated:
        return HttpResponseRedirect("/login/")

    project = Project.objects.get(id=id)
    if project:
        return render(response, "main/project-index.html", {"project":project})

    return render(response, "main/home.html", {})

'''
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
'''
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

# create a project
def project(response):
    if not response.user.is_authenticated:
        return HttpResponseRedirect("/login/")

    if response.method == "POST":
        if response.POST.get("save"):
            my_name = response.POST.get("name")
            my_description = response.POST.get("description")
            my_members_list = response.POST.getlist("members")
            # if the creator did not add theirself, then add them
            if response.user.username not in my_members_list:
                my_members_list.append(response.user.username)

            project = Project(name=my_name, description=my_description,
                creator=response.user, members=my_members_list)
            project.save()
            response.user.project.add(project)


        return HttpResponseRedirect("/project/%i" %project.id) # TODO: redirect to project view
    else:
        form = CreateNewProject()

    # get all users
    User = get_user_model()
    users = User.objects.all()
    return render(response, "main/project.html", {"form":form, "users": users})


def view(response):
    if not response.user.is_authenticated:
        return HttpResponseRedirect("/login/")
    return render(response, "main/view.html", {})
