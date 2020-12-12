from django.contrib import admin, messages
from plans.models import DayPlan, WeeklyPlan
from recipes.models import Recipe
import csv

from django.http import HttpResponse
from io import StringIO


# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    actions = ["get_shop_list_divided_by_meal", "show_shop_list"]

    def get_shop_list_divided_by_meal(self, request, queryset):
        for obj in queryset:
            self.message_user(request, f"Hello world {obj.get_shop_list_divided_by_meal()}", messages.INFO)

    def show_shop_list(self, request, queryset):
        for obj in queryset:
            readable_list = "".join([f"{item['name']} {item['measurement']}: {item['quantity']} "
                                     for item in obj.get_shop_list()])
            self.message_user(request, readable_list, messages.INFO)

    get_shop_list_divided_by_meal.short_description = "Show shop list divided by breakfast, lunch, dinner"
    show_shop_list.short_description = "Show shop list"


class WeeklyAdmin(admin.ModelAdmin):
    actions = ["show_shop_list_divided_by_days", "show_shop_list", "download_shop_list"]

    def show_shop_list_divided_by_days(self, request, queryset):
        for obj in queryset:
            self.message_user(request, obj.get_shop_list_divided_by_days(), messages.INFO)

    def show_shop_list(self, request, queryset):
        for obj in queryset:
            readable_list = "".join([f" {item['name']} {item['measurement']}: {item['quantity']} "
                                     for item in obj.get_shop_list()])
            self.message_user(request, readable_list, messages.INFO)

    def download_shop_list(self, request, queryset):

        f = StringIO()
        writer = csv.writer(f)
        writer.writerow(["name", "measurement", "quantity"])

        for obj in queryset:
            obj.get_shop_list()
            [writer.writerow([item["name"], item["measurement"], item["quantity"]])
             for item in obj.get_shop_list()]
        # move the cursor over it data like seek(0) for start of file
        f.seek(0)
        response = HttpResponse(f, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=shop_list.csv'
        return response

    show_shop_list_divided_by_days.short_description = "show_shop_list_divided_by_days"
    show_shop_list.short_description = "show_shop_list"
    download_shop_list.short_description = "download shop list"

admin.site.register(DayPlan, AuthorAdmin)
admin.site.register(WeeklyPlan, WeeklyAdmin)
