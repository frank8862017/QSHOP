from django.db import models

# Create your models here.

#卖家表
class ManagerMessage(models.Model):
    # 卖家登录用户名
    username=models.CharField(max_length=30)
    # 卖家登录密码
    userpass=models.CharField(max_length=32)
    # 卖家昵称
    nicheng=models.CharField(max_length=30,null=True)
    # 卖家商铺名称
    shop_name=models.CharField(max_length=50,null=True)
    # 卖家商铺logo
    shop_logo=models.ImageField(max_length=50,null=True,upload_to='media/uploads')
    # 卖家商铺地址
    shop_address=models.CharField(max_length=100,null=True)
    #角色id
    role = models.ForeignKey('roles',default=1)


#权限表
class power(models.Model):
    name=models.CharField(max_length=50)
    url=models.CharField(max_length=50)
    add_time=models.DateTimeField(auto_now_add=True)
    add_user=models.CharField(max_length=50)


#角色表
class roles(models.Model):
    name=models.CharField(max_length=30)
    add_time=models.DateTimeField(auto_now=True)
    add_user=models.CharField(max_length=50)
    #逻辑删除
    disabled=models.BooleanField(default=False)

#权限和角色的关系表
class power_roles(models.Model):
    power=models.ForeignKey('power',default=1)
    role=models.ForeignKey('roles',default=1)

