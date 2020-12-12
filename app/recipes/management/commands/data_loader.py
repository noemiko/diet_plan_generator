import json
import copy
from django.core.management.base import BaseCommand, CommandError
from recipes.models import Recipe, RecipeIngredient
from ingredients.models import Protein, Ingredients, Vegetable, Fruit, Meat
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
        receipt_ingredients = receipt.pop("ingredients")
        created_receipt, is_new = Recipe.objects.get_or_create(
            **receipt,
            defaults={"name": receipt["name"]}
        )
        ingredients_classes = extract_ingredients(receipt_ingredients)
        for ingredient, details in ingredients_classes:
            RecipeIngredient.objects.get_or_create(**details, receipt=created_receipt, component=ingredient)


def extract_ingredients(receipt_ingredients):
    ingredients_classes = []
    for i in Ingredients.__subclasses__():
        ingredients_classes.append(i)
    for i in Protein.__subclasses__():
        ingredients_classes.append(i)
    for i in Vegetable.__subclasses__():
        ingredients_classes.append(i)
    for i in Meat.__subclasses__():
        ingredients_classes.append(i)
    classes = {}
    for i in ingredients_classes:
        classes.update({i.__name__: i})
    for ingredients_type, ingredients in receipt_ingredients.items():
        try:
            ingredient_class = classes[ingredients_type]
        except KeyError:
            raise UnknownIngredient(ingredients_type)
        for ingredient in ingredients:
            created, is_created = ingredient_class.objects.get_or_create(name=ingredient["name"])
            yield created, dict(measurement=ingredient["measurement"], quantity=ingredient["quantity"])
