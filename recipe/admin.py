from django.contrib import admin
from recipe.models import Recipe


class ListRecipes(admin.ModelAdmin):
    list_display = ('id', 'name', 'time_prepare')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('category',)
    list_per_page = 2

admin.site.register(Recipe, ListRecipes)
