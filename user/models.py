from django.db import models

class users(models.Model):
    class Meta:
        verbose_name="用户信息"
        verbose_name_plural="用户信息"
    username=models.CharField(max_length=20,verbose_name="用户名")
    email=models.EmailField(default='',max_length=50,verbose_name="用户邮箱")
    is_activate=models.BooleanField(default=0,verbose_name="是否登陆状态")
    password=models.CharField(max_length=32,verbose_name="用户密码")


class car(models.Model):
    class Meta:
        verbose_name="购物车"
        verbose_name_plural="购物车"
    goods=models.ForeignKey('goods.GoodsInfo',default=1,verbose_name="商品",on_delete=models.DO_NOTHING)
    users=models.ForeignKey('users',default=1,verbose_name="用户",on_delete=models.DO_NOTHING)
    number=models.IntegerField("数量")


class  orders(models.Model):
    class Meta:
        verbose_name="订单"
        verbose_name_plural="订单"
    order_code=models.CharField(max_length=14,unique=True,verbose_name="订单编号")
    money=models.DecimalField(max_digits=10,decimal_places=2,verbose_name="总价") #小数点后保留两位
    users=models.ForeignKey('users',default=1,verbose_name="买家",on_delete=models.DO_NOTHING)
    add_time=models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    address=models.CharField(max_length=150,verbose_name="收货地址")
    contacts=models.CharField(max_length=30,default='',verbose_name="收货人")
    phone=models.CharField(max_length=20,default='',verbose_name="收货人电话")
    pay_status=models.BooleanField(default=False,verbose_name="支付状态")
    pay_time=models.DateTimeField(null=True,verbose_name="付款时间")
    send_status=models.BooleanField(default=False,verbose_name="发货状态")
    send_time = models.DateTimeField(null=True,verbose_name="发货时间")
    receive_status=models.BooleanField(default=False,verbose_name="收获状态")
    receive_time=models.DateTimeField(null=True,verbose_name="收货时间")
    comment_status=models.BooleanField(default=False,verbose_name="评价状态")
    manage=models.ForeignKey('manager.ManagerMessage',default=1,verbose_name="商家",on_delete=models.DO_NOTHING)


class order_info(models.Model):
    class Meta:
        verbose_name = "订单详情"
        verbose_name_plural = "订单详情"
    order=models.ForeignKey('orders',default=1,verbose_name="订单编号",on_delete=models.DO_NOTHING)
    goods=models.ForeignKey('goods.GoodsInfo',default=1,verbose_name="商品",on_delete=models.DO_NOTHING)
    number=models.IntegerField(default=1,verbose_name="数量")
    price=models.DecimalField(max_digits=10,decimal_places=2,verbose_name="价格")



class user_address(models.Model):
    class Meta:
        verbose_name = "用户地址"
        verbose_name_plural = "用户地址"
    address=models.CharField(max_length=150,verbose_name="地址")
    users=models.ForeignKey('users',default=1,verbose_name="买家",on_delete=models.DO_NOTHING)
    name=models.CharField(max_length=30,default='',verbose_name="收件人姓名")
    phone=models.CharField(max_length=20,default='',verbose_name="收件人电话")


class comment(models.Model):
    class Meta:
        verbose_name = "买家评价"
        verbose_name_plural = "买家评价"
    goods=models.ForeignKey('goods.GoodsInfo',default=1,verbose_name="商品",on_delete=models.DO_NOTHING)
    manager=models.ForeignKey('manager.ManagerMessage',default=1,verbose_name="商家",on_delete=models.DO_NOTHING)
    users=models.ForeignKey('users',default=1,verbose_name="买家",on_delete=models.DO_NOTHING)
    score=models.IntegerField(default=0,verbose_name="分数")
    content=models.CharField(max_length=100,default='',verbose_name="内容")
    add_time=models.DateTimeField(auto_now_add=True,verbose_name="评价时间")
    status=models.BooleanField(default=False,verbose_name="状态")

