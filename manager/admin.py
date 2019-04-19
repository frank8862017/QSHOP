# from django.contrib import admin
# from .models import ManagerMessage
#
# @admin.register(ManagerMessage)
# class ManagerMessageAdmin(admin.ModelAdmin):
#     list_display = ('username','nicheng','shop_name','shop_address')
#     def get_readonly_fields(self, request, obj=None):
#         if self.obj:
#             return ['username','userpass','nicheng','shop_name','shop_address','role']
#         return []
