import pytest
from recipes.models import Recipe, RecipeIngredient

pytestmark = pytest.mark.django_db

@pytest.mark.django_db
def test_creating_receipt():
    simple_receipt = Recipe.objects.get(name="Frytki z Yama")
    ingredients = simple_receipt.get_ingredients()
    assert ingredients["starch"] == [{"name": "bulwa yam", "measurement": "items", "quantity": 1.0}]
    assert ingredients["meat"] == []
    assert ingredients["vegetables"] == []
    assert ingredients["spices"] == []
    assert ingredients["rest"] == []
