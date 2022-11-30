from django.contrib import admin
from peoples.models import People


class ListOfPeoples(admin.ModelAdmin):
    list_display = ('id', 'name', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 2


admin.site.register(People, ListOfPeoples)
