from django.db import models
from ingredients.models import Ingredients
from itertools import groupby
from collections import defaultdict
from operator import itemgetter


class Recipe(models.Model):
    BREAKFAST = "breakfast"
    LUNCH = "lunch"
    DESSERT = "dessert"
    SNACK = "snack"
    ADDITION = "addition"
    DINNER = "dinner"

    TYPES = [
        (BREAKFAST, "breakfast"),
        (LUNCH, "lunch"),
        (DESSERT, "dessert"),
        (SNACK, "snack"),
        (ADDITION, "addition"),
        (DINNER, "dinner"),
    ]

    DIET = [
        ("AIP", "AIP"),
        ("NORMAL", "NORMAL")
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    type = models.CharField(max_length=9, choices=TYPES)
    components = models.ManyToManyField(Ingredients, through='RecipeIngredient')
    diet_name = models.CharField(max_length=6, choices=DIET, default="AIP")

    def __str__(self):
        return self.name

    def get_ingredients_divided_by_types(self):
        shop_list = defaultdict(list)
        ingredients = self.get_ingredients()
        sorted_by_type = sorted(ingredients, key=itemgetter('type'))
        for type_, ingredients in groupby(sorted_by_type, key=itemgetter('type')):
            for name, ingredients_ in groupby(sorted(ingredients, key=itemgetter('name')), key=itemgetter('name')):
                for measurement, ingredients__ in self.group_by_measurement(ingredients_):
                    quantity = sum(x["quantity"] for x in ingredients__)
                    new_type_ingredients = [{'name': name, 'measurement': measurement, 'quantity': quantity}]
                    if previous_ingredients := shop_list[type_]:
                        new_type_ingredients.extend(previous_ingredients)
                    shop_list.update({type_: new_type_ingredients})
        return shop_list

    def group_by_measurement(self, ingredients):
        sorted_by_measurement = sorted(ingredients, key=itemgetter('measurement'))
        return groupby(sorted_by_measurement, key=itemgetter('measurement'))

    def get_ingredients(self):
        for receipt_component in self.recipeingredient_set.all():
            if not receipt_component.component.types:
                type_ = "unknown"
            else:
                type_ = receipt_component.component.types[0]
            yield {
                "name": receipt_component.component.name,
                "measurement": receipt_component.measurement,
                "quantity": receipt_component.quantity,
                "type": type_}


class RecipeIngredient(models.Model):
    MEASUREMENTS = [
        ("small spoon", "small spoon"),
        ("big spoon", "big spoon"),
        ("grams", "grams"),
        ("kilograms", "kilograms"),
        ("items", "items"),
        ("slices", "slices"),
        ("glasses", "glasses"),
        ("cm", "cm"),
        ("can", "can"),
        ("ml", "ml"),
        ("bunch", "bunch")

    ]
    component = models.ForeignKey(Ingredients, on_delete=models.CASCADE, default=None)
    quantity = models.FloatField()
    measurement = models.CharField(max_length=11, choices=MEASUREMENTS, default="grams")
    receipt = models.ForeignKey(Recipe, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f"{self.id} {self.receipt.name}"
