
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login,name='login'),
    path('dologin/',views.dologin,name='dologin'),
    path('main/',views.main,name="main"),
    path('loginout/',views.loginout,name='loginout'),
    path('order_list/', views.order_list, name='order_list'),
    path('order_info/', views.order_info, name='order_info'),
    path('edit_send_status/', views.edit_send_status, name='edit_send_status'),
    path('comment_list/', views.comment_list, name='comment_list'),
    path('comment_list_yes/', views.comment_list_yes, name='comment_list_yes'),
    path('check_comment/', views.check_comment, name='check_comment'),
    path('edit_count/<int:g_id>', views.edit_count, name='edit_count'),
    path('do_edit_count/<int:g_id>', views.do_edit_count, name='do_edit_count'),
    path('member_list/', views.member_list, name='member_list'),
    path('member_edit/', views.member_edit, name='member_edit'),
    path('do_member_edit/', views.do_member_edit, name='do_member_edit'),
    path('member_del/', views.member_del, name='member_del'),
]
app_name="manager"