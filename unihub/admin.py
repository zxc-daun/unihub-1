from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import *


class ClubAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'contact_email', 'contact_phone', 'location', 'instagram', 'category',
                    'image', 'constitution',)


admin.site.register(Club, ClubAdmin)


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name')
    search_fields = ('email', 'first_name', 'last_name')


admin.site.register(CustomUser, CustomUserAdmin)


class ClubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(ClubCategory, ClubCategoryAdmin)
