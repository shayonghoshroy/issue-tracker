# Generated by Django 3.2.3 on 2021-05-23 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210523_0403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(null=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='file',
            name='file_name',
            field=models.CharField(max_length=200),
        ),
    ]