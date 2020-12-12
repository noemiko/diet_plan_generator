# Generated by Django 3.0.7 on 2020-12-12 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ingredients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('type', models.CharField(choices=[('breakfast', 'breakfast'), ('lunch', 'lunch'), ('dessert', 'dessert'), ('snack', 'snack'), ('addition', 'addition'), ('dinner', 'dinner')], max_length=9)),
                ('diet_name', models.CharField(choices=[('AIP', 'AIP'), ('NORMAL', 'NORMAL')], default='AIP', max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='RecipeIngredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField()),
                ('measurement', models.CharField(choices=[('small spoon', 'small spoon'), ('big spoon', 'big spoon'), ('grams', 'grams'), ('kilograms', 'kilograms'), ('items', 'items'), ('slices', 'slices'), ('glasses', 'glasses'), ('cm', 'cm'), ('can', 'can'), ('ml', 'ml'), ('bunch', 'bunch')], default='grams', max_length=11)),
                ('component', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='ingredients.Ingredients')),
                ('receipt', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='recipes.Recipe')),
            ],
        ),
        migrations.AddField(
            model_name='recipe',
            name='components',
            field=models.ManyToManyField(through='recipes.RecipeIngredient', to='ingredients.Ingredients'),
        ),
    ]
