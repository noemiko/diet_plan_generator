import pytest
from recipes.models import Recipe
from plans.models import DayPlan

pytestmark = pytest.mark.django_db


@pytest.mark.django_db
def test_shop_list_divided_by_meal_when_one_ingredient():
    simple_receipt = Recipe.objects.get(name="Frytki z Yama")
    plan = DayPlan.objects.create(
        breakfast=simple_receipt,
        lunch=simple_receipt,
        dinner=simple_receipt)
    ingredients = plan.get_shop_list_divided_by_meal()
    assert ingredients["breakfast"] == [{"name": "bulwa yam", "measurement": "items", "quantity": 1.0}]
    assert ingredients["lunch"] == [{"name": "bulwa yam", "measurement": "items", "quantity": 1.0}]
    assert ingredients["dinner"] == [{"name": "bulwa yam", "measurement": "items", "quantity": 1.0}]


@pytest.mark.django_db
def test_shop_list_divided_by_ingredient_types_when_one_ingredient():
    simple_receipt = Recipe.objects.get(name="Frytki z Yama")
    empty_receipt = Recipe.objects.create(name="Empty")
    plan = DayPlan.objects.create(
        breakfast=simple_receipt,
        lunch=empty_receipt ,
        dinner=empty_receipt )
    ingredients = plan.get_shop_list_divided_by_types()
    assert ingredients["starch"] == [{"name": "bulwa yam", "measurement": "items", "quantity": 1.0}]
    assert ingredients["meat"] == []
    assert ingredients["vegetables"] == []
    assert ingredients["spices"] == []

#
# @pytest.mark.django_db
# def test_sum_day_shop_list_when_one_ingredient():
#     simple_receipt = Recipe.objects.get(name="Frytki z Yama")
#     plan = DayPlan.objects.create(
#         breakfast=simple_receipt,
#         lunch=simple_receipt,
#         dinner=simple_receipt)
#     ingredients = plan.get_shop_list()
#     assert ingredients == [{"name": "bulwa yam", "measurement": "items", "quantity": 3.0}]


@pytest.mark.django_db
def test_day_shop_list_divided_by_meals_on_multiply_ingredients():
    simple_receipt = Recipe.objects.get(name="Chlebki z ziemniaków taro")
    plan = DayPlan.objects.create(
        breakfast=simple_receipt,
        lunch=simple_receipt,
        dinner=simple_receipt)
    ingredients = plan.get_shop_list_divided_by_meal()
    meals_expected_ingredients = [{'name': 'sól', 'measurement': 'small spoon', 'quantity': 1.0},
                                  {'name': 'pietruszka', 'measurement': 'bunch', 'quantity': 0.5},
                                  {'name': 'ziemniaki taro', 'measurement': 'grams', 'quantity': 750.0},
                                  {'name': 'mąka bananowa', 'measurement': 'grams', 'quantity': 50.0},
                                  {'name': 'cebula', 'measurement': 'items', 'quantity': 1.0}]
    assert ingredients["breakfast"] == meals_expected_ingredients
    assert ingredients["lunch"] == meals_expected_ingredients
    assert ingredients["dinner"] == meals_expected_ingredients


@pytest.mark.django_db
def test_shop_list_divided_by_ingredient_types_when_multiply_ingredient():
    simple_receipt = Recipe.objects.get(name="Chlebki z ziemniaków taro")
    plan = DayPlan.objects.create(
        breakfast=simple_receipt,
        lunch=simple_receipt,
        dinner=simple_receipt)
    ingredients = plan.get_shop_list_divided_by_types()
    print(ingredients)
    assert ingredients["starch"] == [{'name': 'ziemniaki taro', 'measurement': 'grams', 'quantity': 2250.0},
                                     {'name': 'mąka bananowa', 'measurement': 'grams', 'quantity': 150.0}]
    assert ingredients["meat"] == []
    assert ingredients["vegetable"] == [{'name': 'cebula', 'measurement': 'items', 'quantity': 3.0}]
    assert ingredients["spices"] == [{'name': 'sól', 'measurement': 'small spoon', 'quantity': 3.0},
                                     {'name': 'pietruszka', 'measurement': 'bunch', 'quantity': 1.5}]
