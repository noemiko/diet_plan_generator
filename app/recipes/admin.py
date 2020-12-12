from django.contrib import admin
from recipes.models import Recipe, RecipeIngredient


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient


class InlineAdmin(admin.ModelAdmin):
    inlines = [
        RecipeIngredientInline,

    ]


admin.site.register(Recipe, InlineAdmin)
