from django.contrib import admin
from .models import Room


class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'create_date')
    search_fields = ('name', 'slug')
    list_filter = ('create_date',)
    prepopulated_fields = {'slug': ('name',)}



admin.site.register(Room, RoomAdmin)
