# from django.contrib import admin
# from  .models import GoodsType
#
# @admin.register(GoodsType)
# class GoodsTypeAdmin(admin.ModelAdmin):
#     list_display = ('type_id','type_name','type_sort')
#     def get_readonly_fields(self, request, obj=None):
#         if self.obj:
#             return ['type_name','type_sort']
#         return []