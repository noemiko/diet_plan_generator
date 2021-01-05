from django.db import models
from ingredients.models import Ingredients


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

    def get_ingredients(self):
        print(self.components)
        print()
        for i in self.recipeingredient_set.all():
            # print(i.objects.select_subclasses(Starch))

            print(type(i.component))
            print(type(i.component.cast()))
            print(type(i))
            # if issubclass(i.__class__, Starch):
            #     return {"starch": i}


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
