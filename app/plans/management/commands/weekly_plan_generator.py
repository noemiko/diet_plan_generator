from django.core.management.base import BaseCommand, CommandError
from recipes.models import Recipe, RecipeIngredient
from plans.models import DayPlan, WeeklyPlan
import random


class Command(BaseCommand):
    help = 'Generate plans'

    def handle(self, *args, **options):
        WEEK_DAYS = 7
        breakfasts = Recipe.objects.filter(type__exact=Recipe.BREAKFAST)
        lunches = Recipe.objects.filter(type__exact=Recipe.LUNCH)
        dinners = Recipe.objects.filter(type__exact=Recipe.DINNER)
        daily_plans = []
        for day_of_week in range(WEEK_DAYS):
            breakfast = random.choice(breakfasts)
            lunch = random.choice(lunches)
            dinner = random.choice(dinners)
            day = DayPlan.objects.create(
                breakfast=breakfast,
                lunch=lunch,
                dinner=dinner
            )
            daily_plans.append(day)

        WeeklyPlan.objects.create(
            monday=daily_plans[0],
            tuesday=daily_plans[1],
            wednesday=daily_plans[2],
            thursday=daily_plans[3],
            friday=daily_plans[4],
            saturday=daily_plans[5],
            sunday=daily_plans[6]
        )

        print("Plan generated")
