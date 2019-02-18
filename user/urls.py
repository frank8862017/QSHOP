from django.conf.urls import url
from . import views

urlpatterns = [
    # 登录页面显示
    url(r'^login/',views.login,name='login'),

    # 注册页面显示
    url(r'^reg/',views.reg,name='reg'),

    # 用户名验证
    url(r'^check_user',views.check_user,name='check_user'),

    #注册页面提交
    url(r'^doreg',views.doreg,name='doreg'),

    # 登录页面提交
    url(r'^dologin',views.dologin,name='dologin'),

    #退出操作
    url(r'^logout/',views.logout,name='logout'),

    #添加购物车
    url(r'^add_car/',views.add_car,name='add_car'),

    #购物车列表
    url(r'^car_list/',views.car_list,name='car_list'),

    #修改购物车商品数量
    url(r'^edit_num/',views.edit_num,name='edit_num'),

    # 删除购物车商品
    url(r'^del_car/',views.del_car,name='del_car'),

    # 清空购物车
    url(r'^clear_car/',views.clear_car,name='clear_car'),

    # 下单 确认页面
    url(r'^place_order/',views.place_order,name='place_order'),

    # 提交订单页面
    url(r'^do_place_order/',views.do_place_order,name='do_place_order'),

    #新增收货地址
    url(r'^add_address/',views.add_address,name='add_address'),

    #保存收货地址
    url(r'^do_add_address/',views.do_add_address,name='do_add_address'),

    #用户全部订单页面
    url(r'^user_order_list/',views.user_order_list,name='user_order_list') ,

    # 用户中心-修改收货状态
    url(r'^edit_receive_status/', views.edit_receive_status, name='edit_receive_status'),

    #用户中心--查看订单详情
    url(r'^user_order_info/',views.user_order_info,name='user_order_info') ,

    # 用户中心--评价页面
    url(r'^comment_view/',views.comment_view,name='comment_view'),

    # 用户中心--保存评价页面
    url(r'^document/',views.document,name='document'),

    #修改密码页面
    url(r'^edit_password/',views.edit_password,name='edit_password'),

    #修改密码页面提交
    url(r'^check_pwd/',views.check_pwd,name='check_pwd'),

    #修改密码的提交
    url(r'^do_edit_pass/',views.do_edit_pass,name='do_edit_pass'),

    # 验证码
    url(r'^verify_code/', views.verify_code,name='verify_code'),

    # 判断验证码
    url(r'^checked_code/', views.checked_code,name='checked_code'),

    #发送邮件
    url(r'^send_msg/',views.send_msg,name='send_msg'),

    #邮箱验证
    url(r'^activate_email',views.activate_email,name='activate_email'),

    # 邮箱验证的提交
    url(r'^send_msg_view/',views.send_msg_view,name='send_msg_view') ,

    # 邮箱验证的提交
    url(r'^return_url/',views.return_url,name='return_url'),

    #地址页面
    url(r'^address/', views.address, name='address'),
]