from django.shortcuts import render,render_to_response
from manager.models import ManagerMessage
from goods.models import GoodsType,GoodsInfo
from django.db.models import Q
from django.http import HttpResponseRedirect

# Create your views here.


# 店铺列表
def store_list(request):
    manager_list = ManagerMessage.objects.filter()
    return render(request, 'store/store_list.html', {'manager_list': manager_list})

# 店铺详情
def store_details(request):
    manager_id=request.GET.get('id',0)
    type_id=request.GET.get('tid',0)
    type_list=GoodsType.objects.filter()

    q=Q()
    q.connector='and'
    q.children.append(('manager_id',manager_id))

    if type_id!=0:
        q.children.append(('type01_id',type_id))

    goods_list=GoodsInfo.objects.filter(q)

    return render_to_response('store/store_details.html', {'type_list':type_list, 'goods_list':goods_list, 'manager_id':manager_id})

