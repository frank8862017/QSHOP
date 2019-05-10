
from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.login,name='login'),
    path('reg/',views.reg,name='reg'),
    path('check_user',views.check_user,name='check_user'),
    path('doreg',views.doreg,name='doreg'),
    path('dologin',views.dologin,name='dologin'),
    path('logout/',views.logout,name='logout'),
    path('add_car/',views.add_car,name='add_car'),
    path('car_list/',views.car_list,name='car_list'),
    path('edit_num/',views.edit_num,name='edit_num'),
    path('del_car/',views.del_car,name='del_car'),
    path('clear_car/',views.clear_car,name='clear_car'),
    path('place_order/',views.place_order,name='place_order'),
    path('do_place_order/',views.do_place_order,name='do_place_order'),
    path('add_address/',views.add_address,name='add_address'),
    path('do_add_address/',views.do_add_address,name='do_add_address'),
    path('user_order_list/',views.user_order_list,name='user_order_list') ,
    path('edit_receive_status/', views.edit_receive_status, name='edit_receive_status'),
    path('user_order_info/',views.user_order_info,name='user_order_info') ,
    path('comment_view/',views.comment_view,name='comment_view'),
    path('document/',views.document,name='document'),
    path('edit_password/',views.edit_password,name='edit_password'),
    path('check_pwd/',views.check_pwd,name='check_pwd'),
    path('do_edit_pass/',views.do_edit_pass,name='do_edit_pass'),
    path('verify_code/', views.verify_code,name='verify_code'),
    path('checked_code/', views.checked_code,name='checked_code'),
    path('send_msg/',views.send_msg,name='send_msg'),
    path('activate_email',views.activate_email,name='activate_email'),
    path('send_msg_view/',views.send_msg_view,name='send_msg_view') ,
    path('address/', views.address, name='address'),
]
app_name="user"