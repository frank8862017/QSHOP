from django.conf.urls import url
from . import views

urlpatterns = [
    # 商品添加页面
    url(r'^goods_add/',views.goods_add,name='goods_add'),

    #  添加商品页面提交操作
    url(r'^dogoods_add/',views.dogoods_add,name='dogoods_add'),

    # 商品列表显示
    url(r'^goods_list/', views.goods_list, name='goods_list'),

    #  商品删除
    url(r'^goods_delete/(?P<pk>\d+)',views.goods_delete,name='goods_delete'),

    #   商品更新显示
    url(r'^goods_modify/(?P<pk>\d+)',views.goods_modify,name='goods_modify'),

    #   商品更新信息提交
    url(r'^dogoods_modify/',views.dogoods_modify,name='dogoods_modify'),

    # 用户注册账号
    url(r'^openstore/',views.openstore,name='openstore'),

    #用户注册信息提交
    url(r'doopenstore/',views.doopenstore,name='doopenstore'),

    #注册成功进行登录
    url(r'welcome/',views.welcome,name='welcome'),

    # 商城分类
    url(r'goods_type/',views.goods_type,name='goods_type'),

    # 商城  商品详情页
    url(r'goods_details/',views.goods_details,name='goods_details'),

    # 鲜果页
    url(r'^fruit', views.fruit, name='fruit'),
    url('^index',views.index,name='index'),
]