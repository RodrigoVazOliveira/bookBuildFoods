from django.contrib import admin
from recipe.models import Recipe


class ListRecipes(admin.ModelAdmin):
    list_display = ('id', 'name', 'time_prepare')
    list_display_links = ('id', 'name')

admin.site.register(Recipe, ListRecipes)
