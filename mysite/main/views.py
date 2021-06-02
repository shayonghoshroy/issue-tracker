from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . models import ToDoList, Item, Project, Issue, Comment, File
from . forms import CreateNewList, CommentForm, FileForm
from django.contrib.auth import get_user_model
import json
from django.core.exceptions import ValidationError
import os

# Create your views here.

# view project by id
def project_index(response, id):
    if not response.user.is_authenticated:
        return HttpResponseRedirect("/login/")

    print(response.POST)
    print(response)

    project = Project.objects.get(id=id)
    if project:
        # if changes detected, update project
        if response.method == 'POST':
            if response.POST.get("save-changes"):
                my_name = response.POST.get("name")
                my_description = response.POST.get("description")
                my_members_list = response.POST.getlist("members")
                if my_name:
                    project.name = my_name
                if my_description:
                    project.description = my_description
                if my_members_list:
                    project.members = my_members_list
                project.save()

            # delete project
            if response.POST.get("delete"):
                project.delete()
                return HttpResponseRedirect("/")

        # get all users
        User = get_user_model()
        users = User.objects.all()
        return render(response, "main/project-index.html", {"project":project, "users": users})

    return render(response, "main/home.html", {})


# view issue by id
def issue_index(response, id, issue_id):
    if not response.user.is_authenticated:
        return HttpResponseRedirect("/login/")

    for root, dirs, files in os.walk("."):
        for filename in files:
            #print(root, dirs, filename)
            pass

    for file in File.objects.all():
        pass
        #print(file.file_name, file.file)


    issue = Issue.objects.get(id=issue_id)
    cf = CommentForm()
    f = FileForm()
    if issue:
        if response.method == 'POST':
            # comments
            if response.POST.get("comment"):
                cf = CommentForm(response.POST or None)
                if cf.is_valid():
                    content = response.POST.get('content')
                    comment = Comment.objects.create(issue=issue, author=response.user, content=content)
                    comment.save()
                    return HttpResponseRedirect("/project/%i/issue/%i" %(issue.project.id, issue_id))
            # file uploads
            if response.POST.get("upload"):
                f = FileForm(response.POST, response.FILES)
                if f.is_valid():
                    file = f.save()
                    issue.files.append(f.data['file_name'])
                    issue.save()
                    print(issue.files)
                    print(response.POST)
                    return HttpResponseRedirect("/project/%i/issue/%i" %(issue.project.id, issue_id))

            # changes to issue's contents
            if response.POST.get("save-changes"):
                print(response.POST)
                my_summary = response.POST.get("summary")
                my_description = response.POST.get("description")
                my_type = response.POST.get("type")
                my_priority = response.POST.get("priority")
                my_assignee = response.POST.get("assignee")
                my_status = response.POST.get("status")

                if my_summary:
                    issue.summary = my_summary
                if my_description:
                    issue.description = my_description
                if my_type:
                    issue.type = my_type
                if my_priority:
                    issue.priority = my_priority
                if my_assignee:
                    issue.assignee = get_user_model().objects.get(username=my_assignee)
                if my_status:
                    issue.status = my_status

                issue.save()

            # delete issue
            if response.POST.get("delete"):
                issue.delete()
                return HttpResponseRedirect("/project/%i/" %issue.project.id)

        # define and pass all possible fields
        types = ["task", "bug"]
        priorities = ["minor", "major", "blocker"]
        statuses = ["assigned", "in-progress", "resolved"]

        return render(response, "main/issue-index.html", {"issue":issue,
            'comment_form':cf, 'file_form':f, 'all_files':File.objects.all(), "types":types, "priorities":priorities, "statuses":statuses})

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

# create an issue
def issue(response, id):
    print(response.POST)
    my_project = Project.objects.get(id=id)
    if response.method == "POST":
        if response.POST.get("save"):
            my_summary = response.POST.get("summary")
            my_description = response.POST.get("description")
            my_type = response.POST.get("type")
            my_priority = response.POST.get("priority")
            my_assignee = response.POST.get("assignee")

            print(response.POST)
            # validate input
            errors = ["", "", ""]
            default = "none"
            if my_type == default:
                errors[0] = "Please choose a type."
            if my_priority == default:
                errors[1] = "Please choose a priority."
            if my_assignee == default:
                errors[2] = "Please choose an assignee."
            for error in errors:
                if error:
                    return render(response, "main/issue.html", {"project":my_project,
                    "error1":errors[0], "error2":errors[1], "error3":errors[2]})

            my_project.issue_set.create(project=my_project, summary=my_summary, description=my_description, type=my_type, priority=my_priority,
                status="assigned", assigner=response.user, assignee=get_user_model().objects.get(username=my_assignee))
            my_project.save()
        return HttpResponseRedirect("/project/%i/" %my_project.id)


    return render(response, "main/issue.html", {"project":my_project})

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


        return HttpResponseRedirect("/project/%i/" %project.id)
    else:
        form = CreateNewList()

    # get all users
    User = get_user_model()
    users = User.objects.all()
    return render(response, "main/project.html", {"form":form, "users": users})


def view(response):
    if not response.user.is_authenticated:
        return HttpResponseRedirect("/login/")
    return render(response, "main/view.html", {})
