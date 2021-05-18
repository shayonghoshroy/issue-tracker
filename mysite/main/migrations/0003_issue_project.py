# Generated by Django 3.2 on 2021-05-17 01:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_todolist_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=1000)),
                ('creator', models.CharField(max_length=200)),
                ('date_created', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('task', 'task'), ('bug', 'bug')], default='task', max_length=4)),
                ('priority', models.CharField(choices=[('blocker', 'blocker'), ('major', 'major'), ('minor', 'minor')], default='minor', max_length=7)),
                ('status', models.CharField(choices=[('assigned', 'assigned'), ('in-progress', 'in-progress'), ('resolved', 'resolved')], default='assigned', max_length=11)),
                ('creator', models.CharField(max_length=200)),
                ('assignee', models.CharField(max_length=200)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_updated', models.DateField(auto_now=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.project')),
            ],
        ),
    ]