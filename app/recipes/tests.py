import pytest
from recipes.models import Recipe, RecipeIngredient
from ingredients.models import Fruit
from recipes.management.commands.data_loader import receipt_serializer
from ingredients.exceptions import UnknownIngredient
pytestmark = pytest.mark.django_db

@pytest.mark.django_db
def test_creating_receipt():
    receipt_name = "Moj wlasny przepis"
    raw_receipt = [{
    "name": receipt_name,
    "description": "Wszystkie składniki włożyć .",
    "type": "breakfast",
    "diet_name": "aip",
    "ingredients": {
      "Fruit": [
        {
          "name": "dojrzały banan",
          "measurement": "items",
          "quantity": 1
        }]
    }
    }]
    receipt_serializer(raw_receipt)
    assert Recipe.objects.get(name=receipt_name)

@pytest.mark.django_db
def test_creating_receipt_only_once():
    receipt_name = "Moj wlasny przepis"
    raw_receipt = [{
    "name": receipt_name,
    "description": "Wszystkie składniki włożyć .",
    "type": "breakfast",
    "diet_name": "aip",
    "ingredients": {
      "Fruit": [
        {
          "name": "dojrzały banan",
          "measurement": "items",
          "quantity": 1
        }]
    }
    }]
    receipt_serializer(raw_receipt)
    receipt_serializer(raw_receipt)
    created_receipt = Recipe.objects.filter(name=receipt_name)
    assert len(created_receipt) == 1

@pytest.mark.django_db
def test_creating_ingredients():
    expected_ingredient_name = "unicorn"
    raw_receipt = [{
    "name": "Moj wlasny przepis",
    "description": "Wszystkie składniki włożyć .",
    "type": "breakfast",
    "diet_name": "aip",
    "ingredients": {
      "Fruit": [
        {
          "name": expected_ingredient_name,
          "measurement": "items",
          "quantity": 1
        }]
    }
    }]
    receipt_serializer(raw_receipt)
    new_one = Fruit.objects.filter(name=expected_ingredient_name)
    assert len(new_one) == 1

@pytest.mark.django_db
def test_creating_ingredients_only_once():
    expected_ingredient_name = "unicorn"
    raw_receipt = [{
    "name": "Moj wlasny przepis",
    "description": "Wszystkie składniki włożyć .",
    "type": "breakfast",
    "diet_name": "aip",
    "ingredients": {
      "Fruit": [
        {
          "name": expected_ingredient_name,
          "measurement": "items",
          "quantity": 1
        }]
    }
    }]
    receipt_serializer(raw_receipt)
    receipt_serializer(raw_receipt)
    new_one = Fruit.objects.filter(name=expected_ingredient_name)
    assert len(new_one) == 1

@pytest.mark.django_db
def test_creating_unknown_ingredient_will_raise():
    expected_ingredient_name = "unicorn"
    raw_receipt = [{
    "name": "Moj wlasny przepis",
    "description": "Wszystkie składniki włożyć .",
    "type": "breakfast",
    "diet_name": "aip",
    "ingredients": {
      "Unicorn": [
        {
          "name": expected_ingredient_name,
          "measurement": "items",
          "quantity": 1
        }]
    }
    }]
    with pytest.raises(UnknownIngredient) as error:
        receipt_serializer(raw_receipt)

@pytest.mark.django_db
def test_creating_receipt_ingredients():
    expected_ingredient_name = "unicorn"
    receipt_name = "Moj wlasny przepis"
    raw_receipt = [{
    "name": receipt_name,
    "description": "Wszystkie składniki włożyć .",
    "type": "breakfast",
    "diet_name": "aip",
    "ingredients": {
      "Fruit": [
        {
          "name": expected_ingredient_name,
          "measurement": "items",
          "quantity": 1
        }]
    }
    }]
    receipt_serializer(raw_receipt)
    created_receipt = Recipe.objects.get(name=receipt_name)
    created_ingredient = Fruit.objects.get(name=expected_ingredient_name)
    components = RecipeIngredient.objects.get(component=created_ingredient, receipt=created_receipt)
    assert components.measurement == "items"
    assert components.quantity == 1

@pytest.mark.django_db
def test_creating_receipt_ingredients_only_once():
    expected_ingredient_name = "unicorn"
    receipt_name = "Moj wlasny przepis"
    raw_receipt = [{
    "name": receipt_name,
    "description": "Wszystkie składniki włożyć .",
    "type": "breakfast",
    "diet_name": "aip",
    "ingredients": {
      "Fruit": [
        {
          "name": expected_ingredient_name,
          "measurement": "items",
          "quantity": 1
        }]
    }
    }]
    receipt_serializer(raw_receipt)
    receipt_serializer(raw_receipt)
    created_receipt = Recipe.objects.get(name=receipt_name)
    created_ingredient = Fruit.objects.get(name=expected_ingredient_name)
    components = RecipeIngredient.objects.get(component=created_ingredient, receipt=created_receipt)
    assert components.measurement == "items"
    assert components.quantity == 1