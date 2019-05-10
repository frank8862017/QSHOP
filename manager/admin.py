from django.contrib import admin
from .models import ManagerMessage

@admin.register(ManagerMessage)
class ManagerMessageAdmin(admin.ModelAdmin):
    list_display = ('username','nicheng','shop_name','shop_address')
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['username','userpass','nicheng','shop_name','shop_address','role']
        return []

from  django.contrib.auth.models import Permission
@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
	list_display = ('id','name', 'codename', )
	ordering=('id',)
	search_fields = ('name', 'codename')