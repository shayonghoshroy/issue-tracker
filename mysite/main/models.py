from django.db import models

# Create your models here. (relation for database)

# todo list object containing item objects
class ToDoList(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):  # override built in toString
        return self.name

# element of todolist
class Item(models.Model):
    # create item_set for each ToDoList
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    
    text = models.CharField(max_length=300)
    complete = models.BooleanField()

    def __str__(self):
        return self.text
