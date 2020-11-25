# Generated by Django 3.0.7 on 2020-11-25 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_auto_20201125_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receiptcomponent',
            name='measurement',
            field=models.CharField(choices=[('small spoon', 'small spoon'), ('big spoon', 'big spoon'), ('grams', 'grams'), ('kilograms', 'kilograms'), ('items', 'items'), ('slices', 'slices'), ('glasses', 'glasses'), ('cm', 'cm')], default='grams', max_length=11),
        ),
    ]
