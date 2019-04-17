from django.shortcuts import render
from goods.models import GoodsInfo


def index(request):
    user_id = request.session.get('U_userid', 0)
    list = GoodsInfo.objects.filter()    #查询所有商品
    return render(request,'goods/index.html',{'list':list,'user_id':user_id})