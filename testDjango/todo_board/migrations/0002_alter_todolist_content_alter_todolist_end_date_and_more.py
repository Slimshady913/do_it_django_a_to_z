# Generated by Django 4.0.4 on 2022-06-09 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_board', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='content',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='is_complete',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='priority',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='user_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
