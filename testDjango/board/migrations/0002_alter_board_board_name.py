# Generated by Django 4.0.4 on 2022-06-08 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='board_name',
            field=models.CharField(default='Free', max_length=32, verbose_name='게시판 종류'),
        ),
    ]