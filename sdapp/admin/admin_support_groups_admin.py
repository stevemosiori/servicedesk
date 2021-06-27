from django.contrib import admin
from sdapp.models import AdminSupportGroups


@admin.register(AdminSupportGroups)
class AdminSupportGroupsAdmin(admin.ModelAdmin):
    pass
