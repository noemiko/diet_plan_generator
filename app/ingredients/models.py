from django.db import models
from django.contrib.postgres.fields import ArrayField


class Ingredients(models.Model):
    VEGETABLE = "vegetable"
    SPICES = "spices"
    PROTEIN = "protein"
    MEAT = "meat"
    FAT = "fat"
    FRUIT = "fruit"
    LIQUID = "liquid"
    STARCH = "starch"

    TYPES = [
        (VEGETABLE, "vegetable"),
        (SPICES, "spices"),
        (PROTEIN, "protein"),
        (MEAT, "meat"),
        (FAT, "fat"),
        (FRUIT, "fruit"),
        (LIQUID, "liquid"),
        (STARCH, "starch"),
    ]

    GREEN_VEGETABLE = "green_vegetable"
    CABBAGE = "cabbage"
    FISH = "fish"
    POULTRY = "poultry"
    RED_MEAT = "red_meat"
    PROTEIN_FRUIT = "protein_fruit"
    UNKNOWN = "unknown"

    SUBTYPES = [
        (GREEN_VEGETABLE, "green_vegetable"),
        (CABBAGE, "lunch"),
        (FISH, "dessert"),
        (POULTRY, "poultry"),
        (RED_MEAT, "red_meat"),
        (PROTEIN_FRUIT, "protein_fruit"),
        (UNKNOWN, "unknown"),
    ]

    RELATIONS = {
        GREEN_VEGETABLE: VEGETABLE,
        CABBAGE: VEGETABLE,
        FISH: MEAT,
        POULTRY: MEAT,
        RED_MEAT: MEAT
    }

    name = models.CharField(max_length=100)
    types = ArrayField(
        models.CharField(max_length=100, choices=TYPES+SUBTYPES, default=UNKNOWN)
    )

    def __str__(self):
        return self.name

#
# class Vegetable(Ingredients):
#     pass
#
#
# class Spices(Ingredients):
#     pass
#
#
# class Pickled(Vegetable):
#     pass
#
#
# class GreenVegetable(Vegetable):
#     pass
#
#
# class Cabbage(Vegetable):
#     pass
#
#
# class Protein(Ingredients):
#     pass
#
#
# class Meat(Protein):
#     pass
#
#
# class Fish(Meat):
#     pass
#
#
# class Poultry(Meat):
#     pass
#
#
# class RedMeat(Meat):
#     pass
#
#
# class ProteinFruit(Protein):
#     pass
#
#
# class Fat(Ingredients):
#     pass
#
#
# class Fruit(Ingredients):
#     pass
#
#
# class Drink(Ingredients):
#     pass
#
#
# class Starch(Ingredients):
#     pass
#
#
# class Liquid(Ingredients):
#     pass
