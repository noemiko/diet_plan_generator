from django.db import models
from ingredients.models import Ingredients


class Receipt(models.Model):
    TYPES = [
        ("breakfast", "breakfast"),
        ("lunch", "lunch"),
        ("desert", "desert"),
        ("snack", "snack"),
    ]

    DIET = [
        ("AIP", "AIP"),
        ("NORMAL", "NORMAL")
    ]

    name = models.CharField(max_length=100)
    description = models.TextField(1000)
    type = models.CharField(max_length=9, choices=TYPES)
    components = models.ManyToManyField(Ingredients, through='ReceiptComponent')
    diet_name = models.CharField(max_length=6, choices=DIET, default="AIP")


class ReceiptComponent(models.Model):
    MEASUREMENTS = [
        ("small spoon", "small spoon"),
        ("big spoon", "big spoon"),
        ("grams", "grams"),
        ("kilograms", "kilograms"),
        ("items", "items"),
        ("slices", "slices"),
        ("glasses", "glasses"),
        ("cm", "cm")
    ]
    component = models.ForeignKey(Ingredients, on_delete=models.CASCADE, default=None)
    quantity = models.FloatField()
    measurement = models.CharField(max_length=11, choices=MEASUREMENTS, default="grams")
    receipt = models.ForeignKey(Receipt, on_delete=models.CASCADE, default=None)
