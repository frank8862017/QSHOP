from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^goods_add/',views.goods_add,name='goods_add'),
    url(r'^dogoods_add/',views.dogoods_add,name='dogoods_add'),
    url(r'^goods_list/', views.goods_list, name='goods_list'),
    url(r'^goods_delete/(?P<pk>\d+)',views.goods_delete,name='goods_delete'),
    url(r'^goods_modify/(?P<pk>\d+)',views.goods_modify,name='goods_modify'),
    url(r'^dogoods_modify/',views.dogoods_modify,name='dogoods_modify'),
    url(r'^openstore/',views.openstore,name='openstore'),
    url(r'doopenstore/',views.doopenstore,name='doopenstore'),
    url(r'welcome/',views.welcome,name='welcome'),
    url(r'goods_type/',views.goods_type,name='goods_type'),
    url(r'goods_details/',views.goods_details,name='goods_details'),
    url(r'^fruit', views.fruit, name='fruit'),
]
app_name="goods"