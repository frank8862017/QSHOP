from django.shortcuts import render,reverse
from  .models import ManagerMessage,roles
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from goods.models import GoodsInfo
from user.models import orders,comment
from django.core.paginator import Paginator
from django.db.models import Q
import datetime
import json
from django.core.mail import send_mail
from QSHOP.check_power import check_power

# 卖家后台登录页面显示
def login(request):
    return render(request,'manager/login.html')

# 卖家后台登录提交操作
def dologin(request):
   username=request.POST['username']
   userpass=request.POST['password']

   user=ManagerMessage.objects.filter(username=username,userpass=userpass)
   if user:
       request.session['username']=username
       request.session['user_id']=user[0].id

       user_power_list = []
       for filiation in user[0].role.power_roles_set.filter():
           # print(power.power_id, power.role_id)
           user_power_list.append(filiation.power.url)

       request.session['user_power_list'] = user_power_list

       return HttpResponseRedirect('/manager/main')
   else:return HttpResponse('用户名或密码错误！')

# 显示后台管理页面
def main(request):
    # 查询  所有商品  条件：商户ID是当前登录用户的ID
    goods_count=GoodsInfo.objects.filter(manager_id=request.session.get('user_id')).count()
    return render(request,'manager/main.html',{'goods_count':goods_count})

# 退出账号
def loginout(request):
    # 清空session
    request.session.clear()

    # 重定向到登录页面
    return HttpResponseRedirect('/manager/login')

    # 记住，应遵循业务逻辑，不应该只看重实现效果,不能只简单返回一个页面
    # return render(request,'manager/reg.html')


@check_power
# 后台订单管理
def order_list(request):
    p=request.GET.get('p',1)
    order_code=request.GET.get('order_code1','')
    pay_status=request.GET.get('pay_status','99')
    send_status=request.GET.get('send_status','99')

    manager_id=request.session.get('user_id',0)
    if manager_id==0:
        return HttpResponseRedirect('/manager/login')

    where=[]
    view_where={}
    q=Q()
    q.connector='and'
    q.children.append(('manage_id',manager_id))
    if order_code!='':
        q.children.append(('order_code',order_code))
        where.append('order_code='+order_code)    #分页链接，上保留检索条件
        view_where['order_code']=order_code

    if pay_status !='99':
        q.children.append(('pay_status',pay_status))
        where.append('pay_status='+pay_status)
        view_where['pay_status']=pay_status
    if send_status !='99':
        q.children.append(('send_status',send_status))
        where.append('send_status='+send_status)
        view_where['send_status']=send_status

    url_where='&'.join(where)   #拼接分页链接的参数

    orderList=orders.objects.filter(q).order_by('id')
    pageObj=Paginator(orderList,2)  #第一个是数据  第二个参数是每页多少个数据
    data=pageObj.page(p)   #p是页码
    return render(request,'manager/order_list.html',
                  {'orderList':data,'url_where':url_where,'view_where':view_where})


#订单详情
def order_info(request):
    # 订单ID
    order_id=request.GET.get('order_id',0)
    if order_id==0:
        return HttpResponse('请选择要查看的订单')

    manager_id=request.session.get('user_id',0)
    if manager_id==0:
         return HttpResponseRedirect('/manager/login')

    info =orders.objects.filter(id=order_id,manage_id=manager_id).first()
    if info==None:
        return HttpResponse('订单不存在')

    return render(request,'manager/order_info.html',{'info':info})


#修改发货状态
def edit_send_status(request):
    order_id=request.POST.get('order_id',0)
    if order_id==0:
        return HttpResponse('请选择要发货的订单！')

    manager_id=request.session.get('user_id',0)
    if manager_id==0:
        return HttpResponseRedirect('/manager/login')

    bool=orders.objects.filter(id=order_id).update(send_status=1,send_time=datetime.datetime.now())
    if bool:
        return HttpResponseRedirect(reverse('manager:order_list'))
    else:
        return HttpResponse('修改失败')

#查询待审核数据
def comment_list(request):
    type=request.GET.get('type',0)
    score=request.GET.get('score','0')
    p=request.GET.get('p',1)
    manager_id=request.session.get('user_id',0)

    if manager_id==0:
        return HttpResponseRedirect('/manager/ogin')

    where=[]
    view_where={}
    q=Q()
    q.connector='and'
    q.children.append(('manager_id',manager_id))

    if score!='0':
        q.children.append(('score',score))
        where.append('score='+score)  #分页连接上保留检索条件
        view_where['score']=score
    q.children.append(('status',0))
    url_where = '&'.join(where)  # 拼接分页连接的参数

    comment_list = comment.objects.filter(q)
    print(comment_list.query)
    pageObj = Paginator(comment_list, 1)
    data = pageObj.page(p)

    return render(request, 'manager/comment_list.html',
                  {'comment_list': data, 'url_where': url_where, "view_where": view_where})

# 查询已审核数据
def comment_list_yes(request):
    score = request.GET.get('score', '0')
    p = request.GET.get('p', 1)
    manager_id = request.session.get('user_id', 0)

    if manager_id == 0:
        return HttpResponseRedirect('/manager/login')

    where = []
    view_where = {}
    q = Q()
    q.connector = 'and'
    q.children.append(('manager_id', manager_id))

    if score != '0':
        q.children.append(('score', score))
        where.append('score=' + score)  # 分页连接 上保留检索条件
        view_where['score'] = score

    q.children.append(('status', 1))

    url_where = '&'.join(where)  # 拼接分页连接的参数

    comment_list = comment.objects.filter(q)
    pageObj = Paginator(comment_list, 1)
    data = pageObj.page(p)

    return render(request, 'manager/comment_list_yes.html',
                  {'comment_list': data, 'url_where': url_where, "view_where": view_where})


# 审核数据
def check_comment(request):
    comment_id = request.POST.get('comment_id', 0)
    data = {}
    if comment_id == 0:
        data['status'] = 1
        data['msg'] = '请选择要审核的评价'
        return HttpResponse(json.dumps(data))

    # 修改状态
    bool = comment.objects.filter(id=comment_id).update(status=1)

    if bool:
        data['status'] = 1
        data['msg'] = '修改成功'
        return HttpResponse(json.dumps(data))
    else:
        data['status'] = 0
        data['msg'] = '修改失败'
        return HttpResponse(json.dumps(data))


#修改库存
def edit_count(request, g_id):
    goods_info = GoodsInfo.objects.filter(id=g_id).first()
    return render(request, 'manager/edit_count.html', {'goods_info': goods_info})

#修改库存的提交
def do_edit_count(request, g_id):
    count = request.POST.get('count', 0)
    bool = GoodsInfo.objects.filter(id=g_id).update(goods_count=count)
    data = {}
    if bool:
        data['status'] = 1
        data['msg'] = '修改成功'
        return JsonResponse(data)
    else:
        data['status'] = 0
        data['msg'] = '修改失败'
        return JsonResponse(data)


# 用户列表
@check_power
def member_list(request):
    # 查询所有用户信息

    user_name = request.GET.get('user_name', '')
    shop_name = request.GET.get('shop_name', '')
    role = request.GET.get('role', '99')
    p = request.GET.get('p', 1)
    # print(p)
    q = Q()
    q.connector = 'and'

    where = []
    view_where = {}

    if user_name != '':
        q.children.append(('username', user_name))
        where.append('username=' + user_name)  # 分页连接 上保留检索条件
        view_where['username'] = user_name

    if shop_name != '':
        q.children.append(('shop_name', shop_name))
        where.append('shop_name=' + shop_name)  # 分页连接 上保留检索条件
        view_where['shop_name'] = shop_name

    if role != '99':
        q.children.append(('role', role))
        where.append('role=' + role)  # 分页连接 上保留检索条件
        view_where['role'] = role

    # print(view_where)
    url_where = '&'.join(where)  # 拼接分页连接的参数

    data = ManagerMessage.objects.filter(q).order_by('id')
    # print(data.query)

    pageObj = Paginator(data, 2)
    list = pageObj.page(p)

    # 查询角色列表
    role_list = roles.objects.filter(disabled=0)

    return render(request, 'manager/member_list.html',
                  {'list': list, 'url_where': url_where, 'view_where': view_where, 'role_list': role_list})


# 显示修改用户页面
def member_edit(request):
    member_id = request.GET.get('member_id', 0)
    member_info = ManagerMessage.objects.filter(id=member_id).first()

    # 查询角色列表
    role_list = roles.objects.filter(disabled=0)

    return render(request, 'manager/member_edit.html', {'member_info': member_info, 'role_list': role_list})


# 执行修改操作
def do_member_edit(request):
    id = request.POST.get('id')
    username = request.POST.get('username')
    userpass = request.POST.get('userpass')
    nicheng = request.POST.get('nicheng')
    shop_name = request.POST.get('shop_name')
    shop_address = request.POST.get('shop_address')
    role = request.POST.get('role')
    bool=ManagerMessage.objects.filter(id=id).update(username=username,
                                                     nicheng=nicheng,
                                                     shop_name=shop_name,
                                                     shop_address=shop_address,
                                                     userpass=userpass,
                                                     role_id=role)
    if bool:
        data = {}
        data['status'] = 1
        data['msg'] = '修改成功！'
        return JsonResponse(data)
    else:
        data = {}
        data['status'] = 0
        data['msg'] = '修改失败！'
        return JsonResponse(data)


@check_power
def member_del(request):
    id = request.GET.get('id')
    bool = ManagerMessage.objects.filter(id=id).delete()

    data = {}
    if bool:
        data['status'] = 1
        data['msg'] = '删除成功'
    else:
        data['status'] = 0
        data['msg'] = '删除失败'

    return JsonResponse(data)
