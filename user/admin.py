from django.contrib import admin
from .models import users,user_address,orders,order_info

@admin.register(users)
class userAdmin(admin.ModelAdmin):
    list_display = ('username','email')
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['username', 'email','password','is_activate']
        return []
@admin.register(orders)
class ordersAdmin(admin.ModelAdmin):
    list_display = ('order_code','money','add_time','pay','colored_status','colored','comment')
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['users','order_code', 'money','add_time','pay_status','pay_time','send_time','receive_status','receive_time','comment_status','address','contacts','phone','send_status','manage']
        return []