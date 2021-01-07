import pytest
from recipes.models import Recipe, RecipeIngredient
from plans.models import DayPlan, WeeklyPlan
from ingredients.models import Ingredients

pytestmark = pytest.mark.django_db


# @pytest.mark.django_db
# def test_weekly_shop_list_divided_by_days():
#     ingredient = Ingredients.objects.create(name="unicorn", types=[Ingredients.MEAT])
#     receipt = Recipe.objects.create(name="Unicorn meat")
#     RecipeIngredient.objects.create(receipt=receipt, component=ingredient, measurement="glass", quantity=1)
#     one_day = DayPlan.objects.create(breakfast=receipt, lunch=receipt, dinner=receipt)
#     week = WeeklyPlan.objects.create(
#         monday=one_day,
#         thursday=one_day,
#         tuesday=one_day,
#         wednesday=one_day,
#         friday=one_day,
#         sunday=one_day,
#         saturday=one_day
#     )
#     shop_list = week.get_shop_list_divided_by_days()
#     assert shop_list["friday"] == [{'measurement': 'glass', 'name': 'unicorn', 'quantity': 3.0}]
#     assert shop_list["monday"] == [{'measurement': 'glass', 'name': 'unicorn', 'quantity': 3.0}]
#     assert shop_list["wednesday"] == [{'measurement': 'glass', 'name': 'unicorn', 'quantity': 3.0}]
#     assert shop_list["thursday"] == [{'measurement': 'glass', 'name': 'unicorn', 'quantity': 3.0}]
#     assert shop_list["tuesday"] == [{'measurement': 'glass', 'name': 'unicorn', 'quantity': 3.0}]
#     assert shop_list["saturday"] == [{'measurement': 'glass', 'name': 'unicorn', 'quantity': 3.0}]
#     assert shop_list["sunday"] == [{'measurement': 'glass', 'name': 'unicorn', 'quantity': 3.0}]


@pytest.mark.django_db
def test_weekly_get_shop_list_divided_by_types():
    ingredient = Ingredients.objects.create(name="unicorn", types=[Ingredients.MEAT])
    receipt = Recipe.objects.create(name="Unicorn meat")
    RecipeIngredient.objects.create(receipt=receipt, component=ingredient, measurement="glass", quantity=1)
    one_day = DayPlan.objects.create(breakfast=receipt, lunch=receipt, dinner=receipt)
    week = WeeklyPlan.objects.create(
        monday=one_day,
        thursday=one_day,
        tuesday=one_day,
        wednesday=one_day,
        friday=one_day,
        sunday=one_day,
        saturday=one_day
    )
    shop_list = week.get_shop_list_divided_by_types()
    assert shop_list["meat"] == [{'measurement': 'glass', 'name': 'unicorn', 'quantity': 21.0}]
    assert shop_list["starch"] == []

@pytest.mark.django_db
def test_weekly_shop_list_divided_by_type_on_multiple_ingredients():
    ingredient = Ingredients.objects.create(name="unicorn", types=[Ingredients.MEAT])
    cream = Ingredients.objects.create(name="krem jagodowy", types=[Ingredients.FRUIT])
    receipt = Recipe.objects.create(name="Unicorn meat")
    RecipeIngredient.objects.create(receipt=receipt, component=ingredient, measurement="glass", quantity=1)
    RecipeIngredient.objects.create(receipt=receipt, component=cream, measurement="small_spoon", quantity=2)
    one_day = DayPlan.objects.create(breakfast=receipt, lunch=receipt, dinner=receipt)
    week = WeeklyPlan.objects.create(
        monday=one_day,
        thursday=one_day,
        tuesday=one_day,
        wednesday=one_day,
        friday=one_day,
        sunday=one_day,
        saturday=one_day
    )
    shop_list = week.get_shop_list_divided_by_types()
    assert shop_list["meat"] == [{'measurement': 'glass', 'name': 'unicorn', 'quantity': 21.0}]
    assert shop_list["fruit"] == [{'measurement': 'small_spoon', 'name': 'krem jagodowy', 'quantity': 42.0}]
