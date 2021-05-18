# Generated by Django 3.2 on 2021-05-17 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_issue_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='date_created',
            field=models.DateTimeField(editable=False),
        ),
        migrations.AlterField(
            model_name='issue',
            name='date_updated',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='project',
            name='date_created',
            field=models.DateTimeField(editable=False),
        ),
    ]