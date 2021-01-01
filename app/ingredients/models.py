from django.db import models


class Ingredients(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Vegetable(Ingredients):
    pass


class Spices(Ingredients):
    pass


class Pickled(Vegetable):
    pass


class GreenVegetable(Vegetable):
    pass


class Cabbage(Vegetable):
    pass


class Protein(Ingredients):
    pass


class Meat(Protein):
    pass


class Fish(Meat):
    pass


class Poultry(Meat):
    pass


class RedMeat(Meat):
    pass


class ProteinFruit(Protein):
    pass


class Fat(Ingredients):
    pass


class Fruit(Ingredients):
    pass


class Drink(Ingredients):
    pass


class Starch(Ingredients):
    pass


class Liquid(Ingredients):
    pass
