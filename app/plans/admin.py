from operator import itemgetter

from django.contrib import admin, messages
from plans.models import DayPlan, WeeklyPlan
import csv

from django.http import HttpResponse
from io import StringIO


class AuthorAdmin(admin.ModelAdmin):
    actions = ["get_shop_list_divided_by_meal", "get_shop_list_divided_by_types"]

    def get_shop_list_divided_by_meal(self, request, queryset):
        for obj in queryset:
            self.message_user(request, f" {obj.get_shop_list_divided_by_meal()}", messages.INFO)

    def show_shop_list(self, request, queryset):
        for obj in queryset:
            readable_list = "".join([f"{item['name']} {item['measurement']}: {item['quantity']} "
                                     for item in obj.get_shop_list()])
            self.message_user(request, readable_list, messages.INFO)

    def get_shop_list_divided_by_types(self, request, queryset):
        for obj in queryset:
            self.message_user(request, obj.get_shop_list_divided_by_types(), messages.INFO)

    get_shop_list_divided_by_types.short_description = "Show shop list divided by" \
                                                       " type of ingredients like meat, vegetables"
    show_shop_list.short_description = "Show shop list"


class WeeklyAdmin(admin.ModelAdmin):
    actions = ["show_shop_list_divided_by_days",
               "show_shop_list", "download_shop_list", "get_shop_list_divided_by_types"]

    # def show_shop_list_divided_by_days(self, request, queryset):
    #     for obj in queryset:
    #         self.message_user(request, obj.get_shop_list_divided_by_days(), messages.INFO)

    def show_shop_list(self, request, queryset):
        for obj in queryset:
            readable_list = "".join([f" {item['name']} {item['measurement']}: {item['quantity']} "
                                     for item in obj.get_shop_list()])
            self.message_user(request, readable_list, messages.INFO)

    def get_shop_list_divided_by_types(self, request, queryset):
        for obj in queryset:
            self.message_user(request, obj.get_shop_list_divided_by_types(), messages.INFO)

    def download_shop_list(self, request, queryset):
        f = StringIO()
        writer = csv.writer(f)
        header = ["name", "measurement", "quantity"]
        writer.writerow(header)

        for obj in queryset:
            shop_list = obj.get_shop_list_divided_by_types()
            for ingredient_type, ingredients in shop_list.items():
                writer.writerow([ingredient_type.upper()])
                formatted_ingredients = [(item["name"], item["measurement"], item["quantity"]) for item in ingredients]
                writer.writerows(formatted_ingredients)
            # move the cursor over it data like seek(0) for start of file
            f.seek(0)
            response = HttpResponse(f, content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename=shop_list.csv'
        return response

    show_shop_list.short_description = "show_shop_list"
    download_shop_list.short_description = "download shop list"
    get_shop_list_divided_by_types.short_description = "get_shop_list_divided_by_types"


admin.site.register(DayPlan, AuthorAdmin)
admin.site.register(WeeklyPlan, WeeklyAdmin)
