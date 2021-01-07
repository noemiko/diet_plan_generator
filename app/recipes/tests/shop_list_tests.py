import pytest
from recipes.models import Recipe, RecipeIngredient

pytestmark = pytest.mark.django_db


@pytest.mark.django_db
def test_get_shop_list_divided_by_type():
    simple_receipt = Recipe.objects.get(name="Frytki z Yama")
    ingredients = simple_receipt.get_ingredients_divided_by_types()
    assert ingredients["starch"] == [{"name": "bulwa yam", "measurement": "items", "quantity": 1.0}]
    assert ingredients["meat"] == []
    assert ingredients["vegetables"] == []
    assert ingredients["spices"] == []
    assert ingredients["rest"] == []


@pytest.mark.django_db
def test_get_shop_list_divided_by_type_on_multiple():
    simple_receipt = Recipe.objects.get(name="Chlebki z ziemniaków taro")
    ingredients = simple_receipt.get_ingredients_divided_by_types()
    assert ingredients["starch"] == [{'name': 'ziemniaki taro', 'measurement': 'grams', 'quantity': 750.0},
                                     {'name': 'mąka bananowa', 'measurement': 'grams', 'quantity': 50.0}]
    assert ingredients["meat"] == []
    assert ingredients["vegetable"] == [{'name': 'cebula', 'measurement': 'items', 'quantity': 1.0}]
    assert ingredients["spices"] == [{'name': 'sól', 'measurement': 'small spoon', 'quantity': 1.0},
                                     {'name': 'pietruszka', 'measurement': 'bunch', 'quantity': 0.5}]
