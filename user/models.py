from django.db import models

# Create your models here.


# 用户账号密码
class users(models.Model):
    username=models.CharField(max_length=20)
    email=models.EmailField(default='',max_length=50)
    is_activate=models.BooleanField(default=0)
    password=models.CharField(max_length=32)

# 购物车
class car(models.Model):
    # 商品id
    goods=models.ForeignKey('goods.GoodsInfo',default=1)
    # 用户ID
    users=models.ForeignKey('users',default=1)
    # 数量
    number=models.IntegerField()

# 订单表
# 单号，总价，下单人，下单时间，收货地址，支付状态，支付时间，发货状态，商家ID
class  orders(models.Model):
    # 单号
    order_code=models.CharField(max_length=14,unique=True)
    # 总价
    money=models.DecimalField(max_digits=10,decimal_places=2) #小数点后保留两位
    # 外键关联下单人ID
    users=models.ForeignKey('users',default=1)
    #下单时间
    add_time=models.DateTimeField(auto_now_add=True)
    #地址
    address=models.CharField(max_length=150)
    # 收货人姓名
    contacts=models.CharField(max_length=30,default='')
    # 联系电话
    phone=models.CharField(max_length=20,default='')
    #支付状态
    pay_status=models.BooleanField(default=False)
    # 支付时间
    pay_time=models.DateTimeField(null=True)
    # 发货状态
    send_status=models.BooleanField(default=False)
    # 发货时间
    send_time = models.DateTimeField(null=True)
    # 收货状态
    receive_status=models.BooleanField(default=False)
    # 收货时间
    receive_time=models.DateTimeField(null=True)
    #评价状态
    comment_status=models.BooleanField(default=False)
    # 外键关联商家ID
    manage=models.ForeignKey('manager.ManagerMessage',default=1)


# 订单详情表
class order_info(models.Model):
    # 订单ID、
    order=models.ForeignKey('orders',default=1)
    # 外键关联商品ID
    goods=models.ForeignKey('goods.GoodsInfo',default=1)
    # 数量
    number=models.IntegerField(default=1)
    # 小计
    price=models.DecimalField(max_digits=10,decimal_places=2)


# 收货地址
class user_address(models.Model):
    # 收货地址
    address=models.CharField(max_length=150)
    # 外键关联用户ID
    users=models.ForeignKey('users',default=1)
    # 收货人姓名
    name=models.CharField(max_length=30,default='')
    # 收货人电话
    phone=models.CharField(max_length=20,default='')


# 商品评价表
class comment(models.Model):
    # 商品编号
    goods=models.ForeignKey('goods.GoodsInfo',default=1)
    # 卖家编号
    manager=models.ForeignKey('manager.ManagerMessage',default=1)
    # 用户编号
    users=models.ForeignKey('users',default=1)
    # 评分
    score=models.IntegerField(default=0)
    # 评价内容
    content=models.CharField(max_length=100,default='')
    # 评价时间
    add_time=models.DateTimeField(auto_now_add=True)
    # 审核状态
    status=models.BooleanField(default=False)

