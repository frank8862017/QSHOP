from django.contrib import admin
from  .models import GoodsType

@admin.register(GoodsType)
class GoodsTypeAdmin(admin.ModelAdmin):
    list_display = ('type_id','type_name','type_sort')
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['type_name','type_sort']
        return []

admin.site.site_header='水果商城管理员页面'
admin.site.site_title='水果商城管理员页面'