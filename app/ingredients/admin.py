from django.contrib import admin
from ingredients.models import Ingredients


# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    pass


admin.site.register(Ingredients, AuthorAdmin)
#
# for i in Protein.__subclasses__():
#     admin.site.register(i, AuthorAdmin)
#
# for i in Vegetable.__subclasses__():
#     admin.site.register(i, AuthorAdmin)
