from django.db import models
from  manager.models import ManagerMessage


# 商品分类表
class GoodsType(models.Model):
    class Meta:
        verbose_name="商品分类"
        verbose_name_plural="商品分类"
    type_id=models.AutoField(auto_created=True,primary_key=True,default='0',db_column='type_id')
    type_name=models.CharField(default='',null=False,max_length=30,verbose_name="类名")
    type_sort=models.IntegerField(default='0',verbose_name="序号")

# 商品表
class GoodsInfo(models.Model):
    class Meta:
        verbose_name="商品详情"
        verbose_name_plural="商品详情"
    goods_num=models.CharField(max_length=20,verbose_name="商品名称")
    goods_name=models.CharField(max_length=200,verbose_name="原价")
    goods_oprice= models.FloatField(verbose_name="现价")
    goods_xprice = models.FloatField(verbose_name="原价")
    goods_count=models.IntegerField(default=0,verbose_name="数量")
    goods_method=models.CharField(max_length=100,verbose_name="存储方法")
    goods_info=models.CharField(max_length=100,verbose_name="商品介绍")
    goods_pic=models.ImageField(upload_to='media/uploads',verbose_name="商品图片")
    goods_address=models.CharField(max_length=50,verbose_name="配送地址")
    goods_content=models.TextField(verbose_name="商品详情")
    type01=models.ForeignKey(GoodsType,default='',db_column='type_id',verbose_name="商品类型",on_delete=models.DO_NOTHING)
    manager=models.ForeignKey(ManagerMessage,default='',verbose_name="卖家",on_delete=models.DO_NOTHING)