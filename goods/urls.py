
from django.urls import path
from . import views

urlpatterns = [
    path('goods_add/',views.goods_add,name='goods_add'),
    path('dogoods_add/',views.dogoods_add,name='dogoods_add'),
    path('goods_list/', views.goods_list, name='goods_list'),
    path('goods_delete/<int:pk>',views.goods_delete,name='goods_delete'),
    path('goods_modify/<int:pk>',views.goods_modify,name='goods_modify'),
    path('dogoods_modify/',views.dogoods_modify,name='dogoods_modify'),
    path('openstore/',views.openstore,name='openstore'),
    path('doopenstore/',views.doopenstore,name='doopenstore'),
    path('welcome/',views.welcome,name='welcome'),
    path('goods_type/',views.goods_type,name='goods_type'),
    path('goods_details/',views.goods_details,name='goods_details'),
    path('fruit/', views.fruit, name='fruit'),
]
app_name="goods"