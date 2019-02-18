from django.db import models
from  manager.models import ManagerMessage

# Create your models here.

# 商品分类表
class GoodsType(models.Model):
    # 类型id
    type_id=models.AutoField(auto_created=True,primary_key=True,default='0',db_column='type_id')
    # 类型名称
    type_name=models.CharField(default='',null=False,max_length=30)
    # 类型排序
    type_sort=models.IntegerField(default='0')

#     商品表
class GoodsInfo(models.Model):
    # 商品编号
    goods_num=models.CharField(max_length=20)
    # 商品名称
    goods_name=models.CharField(max_length=200)
    # 商品原价
    goods_oprice= models.FloatField()
    # 商品现价
    goods_xprice = models.FloatField()
    # 库存
    goods_count=models.IntegerField(default=0)
    # 存储方法
    goods_method=models.CharField(max_length=100)
    # 商品介绍
    goods_info=models.CharField(max_length=100)
    # 商品缩略图
    goods_pic=models.ImageField(upload_to='media/uploads')
    # 配送地址
    goods_address=models.CharField(max_length=50)
    # 商品内容
    goods_content=models.TextField(30)
    # 商品类型
    type01=models.ForeignKey(GoodsType,default='',db_column='type_id')
    # 关联卖家
    manager=models.ForeignKey(ManagerMessage,default='')