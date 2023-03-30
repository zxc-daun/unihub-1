from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import *


class ClubAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'contact_email', 'contact_phone', 'location', 'instagram', 'category',
                    'image', 'constitution',)
    list_display_links = ('id', 'name')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Club, ClubAdmin)


class ClubCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(ClubCategory, ClubCategoryAdmin)


# Extend UserAdmin to customize User fields in the admin panel
class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name')
    search_fields = ('email', 'first_name', 'last_name')


# Unregister the original User admin and register the customized User admin
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
