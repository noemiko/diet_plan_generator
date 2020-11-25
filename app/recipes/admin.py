
from django.contrib import admin
from recipes.models import Receipt,ReceiptComponent
from ingredients.models import Ingredients
# Register your models here.
# class AuthorAdmin(admin.ModelAdmin):
#     pass

class BookInline(admin.TabularInline):
    model = ReceiptComponent

class BookInline2(admin.TabularInline):
    model = Ingredients

class AuthorAdmin(admin.ModelAdmin):
    inlines = [
        BookInline,

    ]
admin.site.register(Receipt, AuthorAdmin)

# admin.site.register(ReceiptComponent, AuthorAdmin)