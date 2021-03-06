# Generated by Django 3.0.7 on 2020-11-25 20:39

from django.db import migrations
from django.core.management import call_command
from diet_plan_generator.settings import BASE_DIR

def forwards_func(apps, schema_editor):
    call_command('data_loader', file_path=BASE_DIR/'recipes/management/commands/cocktails.json', verbosity=2)
    call_command('data_loader', file_path=BASE_DIR/'recipes/management/commands/dinners.json', verbosity=2)
    call_command('data_loader', file_path=BASE_DIR/'recipes/management/commands/breakfasts.json', verbosity=2)
    call_command('data_loader', file_path=BASE_DIR/'recipes/management/commands/soups.json', verbosity=2)
    call_command('data_loader', file_path=BASE_DIR/'recipes/management/commands/lunches.json', verbosity=2)



def reverse_func(apps, schema_editor):
    print('reverse')


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func, elidable=False)
    ]
