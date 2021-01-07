from recipes.models import Recipe, RecipeIngredient
from django.contrib import admin, messages


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient


class InlineAdmin(admin.ModelAdmin):
    inlines = [
        RecipeIngredientInline,

    ]
    actions = ["show_shop_list_divided_by_types"]

    def show_shop_list_divided_by_types(self, request, queryset):
        for obj in queryset:
            self.message_user(request, obj.get_ingredients_divided_by_types(), messages.INFO)

    show_shop_list_divided_by_types.short_description = "Show shop list divided by" \
                                                      " type of ingredients like meat, vegetables"
admin.site.register(Recipe, InlineAdmin)
