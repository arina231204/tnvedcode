from django.contrib import admin
from .models import TnvedCode, Organization, Permission

class PermissionAdmin(admin.ModelAdmin):
    list_display = ('code', 'organization', 'import_status_legal', 'import_status_individual')

admin.site.register(TnvedCode)
admin.site.register(Organization)
admin.site.register(Permission, PermissionAdmin)