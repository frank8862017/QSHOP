from django.db import models

class ManagerMessage(models.Model):
    class Meta:
        verbose_name="商家信息"
        verbose_name_plural="商家信息"
    username=models.CharField(max_length=30,verbose_name="用户名")
    userpass=models.CharField(max_length=32,verbose_name="密码")
    nicheng=models.CharField(max_length=30,null=True,verbose_name="昵称")
    shop_name=models.CharField(max_length=50,null=True,verbose_name="店铺名")
    shop_logo=models.ImageField(max_length=50,null=True,upload_to='media/uploads',verbose_name="店铺logo")
    shop_address=models.CharField(max_length=100,null=True,verbose_name="店铺地址")
    role = models.ForeignKey('roles',default=1,verbose_name="角色",on_delete=models.DO_NOTHING)
    def __str__(self):
        return self.username

class power(models.Model):
    name=models.CharField(max_length=50)
    url=models.CharField(max_length=50)
    add_time=models.DateTimeField(auto_now_add=True)
    add_user=models.CharField(max_length=50)

class roles(models.Model):
    name=models.CharField(max_length=30)
    add_time=models.DateTimeField(auto_now=True)
    add_user=models.CharField(max_length=50)
    disabled=models.BooleanField(default=False)
    def __str__(self):
        return self.name

class power_roles(models.Model):
    power=models.ForeignKey('power',default=1,on_delete=models.DO_NOTHING)
    role=models.ForeignKey('roles',default=1,on_delete=models.DO_NOTHING)

