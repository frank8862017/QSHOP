from django.conf.urls import url
from . import views
# from django.contrib import admin

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    #店铺列表
    url(r'^store_list/',views.store_list,name='store_list'),

    #店铺详情
    url(r'^store_details/',views.store_details,name='store_details'),
]
app_name="store"