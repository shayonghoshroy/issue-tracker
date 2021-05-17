from main.models import ToDoList, Item, Project, Issue

def create_issue():
	i = Issue(project=Projects.objects.get(id=1), type="task", priority="blocker",status="assigned",creator="shayon", assignee="tristan")
	i.save()
	print(i)

create_issue()
