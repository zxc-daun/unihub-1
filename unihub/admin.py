from django.contrib import admin
from .models import *


class ClubAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'contact_email', 'contact_phone', 'location', 'instagram', 'category',
                    'image', 'constitution',)


admin.site.register(Club, ClubAdmin)


class ClubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(ClubCategory, ClubCategoryAdmin)
