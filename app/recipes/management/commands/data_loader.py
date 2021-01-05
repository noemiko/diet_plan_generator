import json
import copy
from django.core.management.base import BaseCommand, CommandError
from recipes.models import Recipe, RecipeIngredient
from ingredients.models import Ingredients
from ingredients.exceptions import UnknownIngredient


class Command(BaseCommand):
    help = 'Load data'

    def add_arguments(self, parser):
        parser.add_argument('-f', '--file_path', type=str, help='Get file path', )

    def handle(self, *args, **options):
        file_path = options["file_path"]
        if not file_path:
            raise CommandError("Missing file path")
        with open(file_path) as f:
            data = json.load(f)
        receipt_serializer(data)
        print(file_path)


def receipt_serializer(receipts):
    receipts = copy.deepcopy(receipts)
    for receipt in receipts:
        receipt_ingredients = receipt.pop("ingredients", {})
        created_receipt, is_new = Recipe.objects.get_or_create(
            **receipt,
            defaults={"name": receipt["name"]}
        )
        ingredients_classes = extract_ingredients(receipt_ingredients)
        for ingredient, details in ingredients_classes:
            print(details)
            RecipeIngredient.objects.get_or_create(**details, receipt=created_receipt, component=ingredient)


def extract_ingredients(receipt_ingredients):
    """
    {'Spices': [{'name': 'cynamon', 'measurement': 'small spoon', 'quantity': 1},
    {'name': 'skórka z pomaranczy', 'measurement': 'small spoon', 'quantity': 0.5}],
    'Fruit': [{'name': 'dojrzały banan', 'measurement': 'items', 'quantity': 1}],
    'Liquid': [{'name': 'mleko koko', 'measurement': 'glass', 'quantity': 1.5}],
    'Starch': [{'name': 'batat', 'measurement': 'glass', 'quantity': 1}]}

    """
    print(receipt_ingredients)
    for ingredient_type, ingredients in receipt_ingredients.items():
        subtypes_names, _ = zip(*Ingredients.SUBTYPES)
        types_names, _ = zip(*Ingredients.TYPES)

        for ingredient in ingredients:
            ingredient_types = []
            ingredient_type = ingredient_type.lower()
            if ingredient_type in subtypes_names:
                ingredient_types.append(ingredient_type)
                if (type_ := Ingredients.RELATIONS.get(ingredient_type)):
                    print(type_)
                    ingredient_types.insert(0, type_)
            elif ingredient_type in types_names:
                ingredient_types.append(ingredient_type)
            print(ingredient_types)
            print(ingredient["name"])
            created, is_created = Ingredients.objects.get_or_create(name=ingredient["name"], types=ingredient_types)
            yield created, dict(measurement=ingredient["measurement"], quantity=ingredient["quantity"])
