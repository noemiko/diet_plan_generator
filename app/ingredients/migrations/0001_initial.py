# Generated by Django 3.0.7 on 2021-01-05 18:02

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('types', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('vegetable', 'vegetable'), ('spices', 'spices'), ('protein', 'protein'), ('snack', 'meat'), ('fat', 'fat'), ('fruit', 'fruit'), ('liquid', 'liquid'), ('starch', 'starch'), ('green_vegetable', 'green_vegetable'), ('cabbage', 'lunch'), ('fish', 'dessert'), ('poultry', 'poultry'), ('red_meat', 'red_meat'), ('protein_fruit', 'protein_fruit'), ('unknown', 'unknown')], default='unknown', max_length=15), size=None)),
            ],
        ),
    ]
