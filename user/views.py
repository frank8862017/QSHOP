from django.shortcuts import render,reverse,render_to_response
from  django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from .models import users,car,user_address,order_info,orders,comment
from django.db.models import Sum
from goods.models import GoodsInfo
import  hashlib
import json
import random
import datetime
from PIL import Image,ImageDraw,ImageFont
from io import BytesIO
from django.core.mail import  send_mail   #发送邮件
import time
#导入支付宝模块
from alipay.aop.api.AlipayClientConfig import AlipayClientConfig
from alipay.aop.api.DefaultAlipayClient import DefaultAlipayClient
from alipay.aop.api.domain.AlipayTradePagePayModel import AlipayTradePagePayModel
from alipay.aop.api.request.AlipayTradePagePayRequest import AlipayTradePagePayRequest
# Create your views here.

# 登录页面
def login(request):
    return  render(request,'user/login.html')

# 注册页面
def reg(request):
    return render(request,'user/reg.html')


# 检查用户是否存在
def check_user(request):
    username=request.GET.get('username')
    info=users.objects.filter(username=username).first()
    if info!=None:
        return HttpResponse('1')
    else:return HttpResponse('0')

# 用户注册页面提交操作
def doreg(request):
    # 获取注册的用户名和密码
    username = request.POST.get('username')
    passwd = request.POST.get('userpass')
    email = request.POST.get('email')

    # 对密码进行加密
    md = hashlib.md5()
    md.update(passwd.encode('utf-8'))
    md5_password = md.hexdigest()

    # 向数据库提交数据
    userObj = users()
    userObj.username = username
    userObj.password = md5_password
    userObj.email=email
    userObj.save()

    request.session['temp_uid']=userObj.id
    return HttpResponseRedirect(reverse('user:send_msg_view'))


#注册邮箱时
def send_msg_view(request):
    uid=request.session.get('temp_uid',0)
    info=users.objects.filter(id=uid).first()
    return render(request,'user/send_msg.html',{'user_info':info})

# 用户登录页面--提交
def dologin(request):
    username=request.POST.get('username')
    passwd=request.POST.get('userpass')

    # 对密码进行加密
    md = hashlib.md5()
    md.update(passwd.encode('utf-8'))
    md5_password = md.hexdigest()

    # 查询数据库  比对用户名和密码
    info =users.objects.filter(username=username,password=md5_password).first()

    if info!=None:
            request.session['U_userid']=info.id
            request.session['U_username']=info.username
            return  HttpResponseRedirect('/')
    else:
        return HttpResponse('用户名或密码有误！')   #出于安全考虑，不能只提示一种错误

# 用户退出登录
def logout(requeset):
    # 清空session值
    requeset.session.clear()
    # 重定向到登录页面
    return HttpResponseRedirect('/user/login')

# 添加购物车
def add_car(request):
    goods_id=request.POST.get('goods_id',0)
    number=request.POST.get('count',0)
    # print(request.POST)

    # 安全验证
    if goods_id==0:
        return  HttpResponse('你要买什么？')

    if number==0:
        return HttpResponse('数量不能为零。')

    user_id=request.session.get('U_userid',0)

    if user_id==0:
        return HttpResponseRedirect('/user/login')

    # 判断商品是否已存在于购物车
    exists=car.objects.filter(goods_id=goods_id,users_id=user_id).first()
    if exists==None:
        carObj=car()
        carObj.goods_id=goods_id
        carObj.users_id=user_id
        carObj.number=number
        carObj.save()
    else:
        exists.number=exists.number + int(number)
        exists.save()
    return HttpResponseRedirect('/user/car_list')

# 购物车列表  显示购物车内的物品
def car_list(request):
    user_id=request.session.get('U_userid',0)
    if user_id==0:
        return HttpResponseRedirect('/user/login')

    list=car.objects.filter(users_id=user_id)
    return render(request,'user/cart_list.html',{'car_list':list})


# 在购物车页面  修改购物车商品的数量
def edit_num(request):
    user_id = request.session.get('U_userid', 0)
    goods_id=request.POST.get('goods_id',0)
    number=int(request.POST.get('number',0))
    type=request.POST.get('type',0)

    # 安全验证
    data={}

    if goods_id==0:
        data['status']=0  #0失败   1成功
        data['msg']='商品ID不能为空'
        return  HttpResponse(json.dumps(data))

    if number==0:
        data['status']=0   #0失败，1成功
        data['msg']='数量不能空'
        return HttpResponse(json.dumps(data))
    if user_id==0:
        data['status']=0  #0失败  1成功
        data['msg']='请登录'
        return HttpResponse(json.dumps(data))

    # 操作数据库
    if type == 'reduce':
        if number>1:
            number = number - 1
    elif type == 'jia' :
        number = number + 1
    else:
        number=number

    good_info=GoodsInfo.objects.filter(id=goods_id).first()
    if good_info.goods_count< number:
        data['status']=0
        data['msg']='库存不足！'
        return JsonResponse(data)
    #操作数据库
    bool=car.objects.filter(goods_id=goods_id,users_id=user_id).update(number=number)
    if bool:
        data['status'] = 1  # 0 失败  1成功
        data['msg'] = '操作成功'
        data['number'] = number
        return HttpResponse(json.dumps(data))
    else:
        data['status'] = 0  # 0 失败  1成功
        data['msg'] = '操作失败，请稍后再试！'
        return HttpResponse(json.dumps(data))


# 删除单条购物车
def del_car(request):
    user_id = request.session.get('U_userid', 0)
    goods_id = request.POST.get('goods_id', 0)

    data={}
    if goods_id == 0:
        data['status'] = 0  # 0失败   1成功   2返回登录页面
        data['msg'] = '商品ID不能为空'
        return HttpResponse(json.dumps(data))

    # 判断是否登录
    if user_id == 0:
        data['status'] = 2  # 0失败  1成功   2返回登录页面
        data['msg'] = '请登录'
        data['data']='/user/login'
        return HttpResponse(json.dumps(data))

    # 数据库操作
    bool=car.objects.filter(users_id=user_id,goods_id=goods_id).delete()
    if bool:
        data['status'] = 1  # 0失败  1成功   2返回登录页面
        data['msg'] = '操作成功！'
        return HttpResponse(json.dumps(data))
    else:
        data['status'] = 0
        data['msg'] = '删除失败。'
        return HttpResponse(json.dumps(data))


# 清空购物车
def clear_car(request):
    data={}
    # 判断是否登录
    user_id = request.session.get('U_userid', 0)
    if user_id == 0:
        data['status'] = 2  # 0失败  1成功   2返回登录页面
        data['msg'] = '请登录'
        data['data'] = '/user/login'
        return HttpResponse(json.dumps(data))

    #数据库操作
    bool=car.objects.filter(users_id=user_id).delete()
    data = {}
    if bool:
        data['status'] = 1  # 0失败  1成功   2返回登录页面
        data['msg']='清空成功。'
        return HttpResponse(json.dumps(data))
    else:
        data['status'] = 0
        data['msg'] = '删除失败。'
        return HttpResponse(json.dumps(data))

# 下单   确认页面
def place_order(request):
    # 查询数据   渲染页面
    # 所有的购物车信息
    user_id=request.session.get('U_userid',0)
    if user_id==0:
        return HttpResponseRedirect('/user/login')

    # 筛选用户商品
    list=car.objects.filter(users_id=user_id)

    total=0
    for cart in list:
        total+=cart.number * int(cart.goods.goods_xprice)

    # 查询用户所有的收货地址
    address_list=user_address.objects.filter(users_id=user_id)
    #  将数据返回
    return render(request,'user/order.html',{'car_list':list,'total_money':total,'address_list':address_list})

# 提交订单操作
def do_place_order(request):
    address_id=request.POST.get('address',0)
    if address_id==0:
        return HttpResponse('请选择收货地址！')

    user_id=request.session.get('U_userid',0)

    if user_id==0:
        return HttpResponseRedirect('/user/login')

    # 根据收货地址的ID查询详情
    address_info=user_address.objects.filter(id=address_id,users_id=user_id).first()
    if address_info==None:
        return HttpResponse('请选择收货地址！')

    # 查询购物车内所有的数据，计算金额
    car_list=car.objects.filter(users_id=user_id)

    if not car_list:
        return HttpResponse('请选择商品!')

    total_money=0
    manage_id=0
    manage_name=''
    goods_name_all=''
    for cart in car_list:
        total_money+=cart.number * int(cart.goods.goods_xprice)
        manage_id=cart.goods.manager_id    #多个商品，最后一个覆盖前边的商品
        manage_name = cart.goods.manager.shop_name
        goods_name_all += cart.goods.goods_name
        goods_info=GoodsInfo.objects.filter(id=cart.goods_id).first()
        if goods_info.goods_count< cart.number:
            return message(goods_info.goods_name + "库存不足，请重新选择<a href='%s'>返回购物车</a>" % (reverse('user:car_list')))

    #库存减少
    for cart in car_list:
        goods_info = GoodsInfo.objects.filter(id=cart.goods_id).first()
        goods_info.goods_count -= cart.number
        result = GoodsInfo.objects.filter(id=cart.goods_id).update(goods_count=goods_info.goods_count)
    if result:
        # 创建订单
        orderObj=orders()
        orderObj.order_code='20181010' + str(random.randint(100000,999999))
        orderObj.money=total_money
        orderObj.users_id=user_id
        orderObj.address=address_info.address
        orderObj.contacts=address_info.name
        orderObj.phone=address_info.phone
        orderObj.manage_id=manage_id
        orderObj.save()
        # 订单详情表
        for cart in car_list:
            orderinfoObj=order_info()
            orderinfoObj.order_id=orderObj.id
            orderinfoObj.number=cart.number
            orderinfoObj.goods_id=cart.goods_id
            orderinfoObj.price=cart.goods.goods_xprice
            orderinfoObj.save()

        # 重定向到首页
        alipay_client_config = AlipayClientConfig()
        alipay_client_config.server_url = 'https://openapi.alipaydev.com/gateway.do'  #
        #手动设置
        alipay_client_config.app_id = '2016092100561600'
        alipay_client_config.app_private_key = 'MIIEpgIBAAKCAQEA6KVS4YuG3pFvhbQHtBLjsgWXNe/Xjg2CVCc4+SfiwMeakR/O5IqZqVPThEl9allFyEHPFK7Anofebe+OO0BdYdGfCSrW0R+B85lEfH5YL2ggy9yCWB3GPiffA6B+UM2nO8HRMs1ulcpUPosCfzIucJUgX1IQZxJmAyTHmXzSoJVtY/1WbpLsP/zQgp+cUkfFi3CFDGxz6ex3w1U2q9SxemiQvUYbnn1EC3Yv3E0APloRrsAm+XIvPKLMacSbfHcZJw9EcaF3uNfNYtKzHGObigAzF1EEZlRbwG5LeOQ/iPJvbLilMyefFamuwgCZDBDTVQmHwA9QrjWjHUdeLZyW6QIDAQABAoIBAQCTZXtXbwEqLlbMDT38NyOP/L7K64RUefaivp74LO8bWNtzKwX4AmBMydFvNOiC4sC1mgxLfFSJnGeum2Iv5B3GBfuO4Vds81twLSEZByt0DbMJtlHW5jZd1wES2TJum31i/O9AEqwHt0McxRH16KNHrRPvkJzX0O5U+46CjnUcS5rZXir/OSDHwcN/cBxGqNhaEVsSSsWME8YOsfhCrVlKgI3vfW8UrEp/KociczM+N9wH0NbUlDgo2J9WuvH6/QyYkrLyO4KY5Bs05odS3wn+SoItOMEL8qROQ1iF9b2H5zYc7Ahd1kDBKGTSLVMw5iXUGBons0+eUCUoveiQF3+hAoGBAPcczgsFo9YuR1QSAjh2BsM9BEG2FAn5/xg4HzJoHEtd8fM4MAnwCGECWkzvNE866OaFs743ReQga9Nds4eI5Cg8019m1XAifzvxLaAK+nkotO+fz/8cNKrwS9pYFXNq2XRVph05r+Z/sSfMUUt4IecfTwjPvlGsWzeNQPjfOfx1AoGBAPEDUm9lHFDLngNIQisiRhIb2yWicJVMqL00rFZVnV6zh3G1Tbbp6EV5zmXS8/wJpmYwoGZO6RLWkMPB4f6YS4Lgi9nEHSxxDaIYvcWPasGywrWQw5r7NWEG71BCLGEG0yOVbOImiHAfC52L1hALtOCH9o7F0Lw2quNdAX4Ks3IlAoGBAJJz/uVnZU9VxC5eMfS2dpGVgwVS3ROAl6AJ+utL6qD8P54PSeFJ4h1kYJJCHnVqi4e76+grJ//o+x6c5P7JsbbrPbbH4m1/9HpZGNpGR2YxKvLtez9NvyUkH0B7fdMWm2QoMrgVbVuliB/3JqMcwrMQyi2Fudz70l/dFomo+tvVAoGBAOZPuV/v7G4dFiOm0mxrtTAq5HGDWDij5//erO1XpSnRP5ZeniQ0RBzYOG8/dp4cDqJKx4zczYeN+QrIZREpMcegkqQH76T/Z/rFz9tRoL/29nARJYsdkbXlrZ0xjz0tC2lOqp02G12hnTTxYx80QKXr56YpzL1/NDBPOVTcHvztAoGBAL29jtznLilUpKZqv5rEaInlBk47SDqb91vjLrsi0nvFTFOspifGkhWJHGvo0RzcSVkRqNUXFamWups+nGjJYMgcOWtktsBaFDqjoOuhC3x5qBH6L/8mNuFCcaDU+I0oJVCvxPcTuzhNXdY0gUFzibsjn56InfJsx+jB7jxEkyan'
        alipay_client_config.alipay_public_key = 'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA6KVS4YuG3pFvhbQHtBLjsgWXNe/Xjg2CVCc4+SfiwMeakR/O5IqZqVPThEl9allFyEHPFK7Anofebe+OO0BdYdGfCSrW0R+B85lEfH5YL2ggy9yCWB3GPiffA6B+UM2nO8HRMs1ulcpUPosCfzIucJUgX1IQZxJmAyTHmXzSoJVtY/1WbpLsP/zQgp+cUkfFi3CFDGxz6ex3w1U2q9SxemiQvUYbnn1EC3Yv3E0APloRrsAm+XIvPKLMacSbfHcZJw9EcaF3uNfNYtKzHGObigAzF1EEZlRbwG5LeOQ/iPJvbLilMyefFamuwgCZDBDTVQmHwA9QrjWjHUdeLZyW6QIDAQAB'
        """
        得到客户端对象。
        注意，一个alipay_client_config对象对应一个DefaultAlipayClient，定义DefaultAlipayClient对象后，alipay_client_config不得修改，如果想使用不同的配置，请定义不同的DefaultAlipayClient。
        logger参数用于打印日志，不传则不打印，建议传递。
        """
        client = DefaultAlipayClient(alipay_client_config=alipay_client_config)

        """
        页面接口示例：alipay.trade.page.pay
        """
        # 对照接口文档，构造请求对象
        model = AlipayTradePagePayModel()
        model.out_trade_no = orderObj.order_code
        model.total_amount = total_money
        model.subject = "Qshop-" + manage_name
        model.body = goods_name_all
        model.product_code = "FAST_INSTANT_TRADE_PAY"
        request = AlipayTradePagePayRequest(biz_model=model)
        request.return_url = 'http://39.105.195.67:80/user/return_url/'
        # 得到构造的请求，如果http_method是GET，则是一个带完成请求参数的url，如果http_method是POST，则是一段HTML表单片段
        response = client.page_execute(request, http_method="GET")
        # print("alipay.trade.page.pay response:" + response)
        # 清空购物车
        car.objects.filter(users_id=user_id).delete()
        return HttpResponseRedirect(response)
    else:
        return HttpResponse('操作有误！')

# 添加收货地址
def add_address(request):
    return render(request,'user/add_address.html')

# 保存收货地址
def do_add_address(request):
    name=request.POST.get('name','')
    address=request.POST.get('address','')
    phone=request.POST.get('phone','')

    # 判断是否填写
    if name=='' or address=='' or phone=='' :
        return HttpResponse('信息不完整！')

    user_id = request.session.get('U_userid', 0)
    if user_id==0:
        return HttpResponseRedirect(reverse('user:login'))

    result=user_address.objects.create(name=name,address=address,users_id=user_id,phone=phone)
    if result:
        return HttpResponseRedirect(reverse('user:place_order'))


# 用户中心的订单管理
def verify_login(func):
    def inner_func(request):
        user_id = request.session.get('U_userid', 0)
        if user_id == 0:
            return HttpResponseRedirect(reverse('user:login'))
        else:
            return func(request)

    return inner_func

@verify_login
def user_order_list(request):
    # 判断是否登录
    user_id = request.session.get('U_userid', 0)

    # 查找订单
    order_list=orders.objects.filter(users_id=user_id)
    return render(request,'user/user_order_list.html',{'order_list':order_list})


# 修改收货状态
def edit_receive_status(request):
    data = {}
    # 判断是否登录
    user_id = request.session.get('U_userid', 0)
    print(user_id)
    if user_id == 0:
        data['status'] = 0 # 0失败  1成功   0
        data['msg'] = '请登录!'
        return HttpResponse(json.dumps(data))

    #判断是否选择订单
    order_id = request.POST.get('order_id', 0)
    print(order_id)
    if order_id==0:
        data['msg']='请选择订单'
        data['status']=0
        return HttpResponse(json.dumps(data))

    bool=orders.objects.filter(id=order_id,users_id=user_id).update(receive_status=1,receive_time=datetime.datetime.now())
    print(bool)
    if bool:
        data['msg']='修改成功！'
        data['status']=1
        return HttpResponse(json.dumps(data))
    else:
        data['msg']='修改失败！'
        data['status']=0
        return HttpResponse(json.dumps(data))


# 商品页
def user_order_info(request):
    order_id=request.GET.get('order_id',0)
    if order_id==0:
        return HttpResponse('请选择要查看的订单')

    user_id=request.session.get('U_userid',0)
    if user_id==0:
        return HttpResponse('请登录！')
    info=orders.objects.filter(id=order_id,users_id=user_id).first()
    list=user_address.objects.filter(id=order_id,users_id=user_id).first()

    if info==None:
        return HttpResponse('未接到订单！')

    # 返回渲染之后的结果
    return render(request,'user/user_order_info.html',{'info':info,'list':list})


# 渲染评价页面
def comment_view(request):
    order_id=request.GET.get('order_id',0)
    print(order_id)
    order_info_list=order_info.objects.filter(order_id=order_id)
    print(order_info_list)
    return render(request,'user/comment.html',{'order_info_list':order_info_list})

# 保存评价
def document(request):
    print(request.POST)
    goods_id_list=request.POST.getlist('goods_id')
    order_id=request.POST.get('order_id',0)

    user_id=request.session.get('U_userid',0)
    if user_id==0:
        return HttpResponse('请登录！')

    for goods_id in goods_id_list:
        score=request.POST.get('score'+goods_id)
        content=request.POST.get('comment_content'+goods_id)
        commentObj=comment()
        commentObj.goods_id=goods_id

        good_info=GoodsInfo.objects.filter(id=goods_id).first()
        commentObj.manager_id=good_info.manager_id

        commentObj.users_id=user_id
        commentObj.score=score
        commentObj.content=content
        commentObj.save()

    #修改订单评价状态
    bool=orders.objects.filter(id=order_id).update(comment_status=1)
    if bool:
        return HttpResponseRedirect(reverse('user:user_order_list'))
    else:
        return HttpResponse('评价状态修改失败！')

# 显示  修改密码页面
def edit_password(request):
    user_id=request.session.get('U_userid',0)
    if user_id==0:
        return HttpResponseRedirect(reverse('user:login'))

    return render(request,'user/updatepass.html')

# 显示  地址页面
def address(request):
    user_id=request.session.get('U_userid',0)
    if user_id==0:
        return HttpResponseRedirect(reverse('user:login'))

    address_list=user_address.objects.filter(users_id=user_id)
    return render(request,'user/address.html',{'address_list':address_list})


#  修改密码的判断
def  check_pwd(request):
    userpass=request.POST.get('userpass',0)
    usernewpass=request.POST.get('usernewpass',0)
    useragainpass=request.POST.get('useragainpass',0)
    print(userpass)
    # 空字典   空集合set()
    data = {}
    # 判断是否登录
    user_id = request.session.get('U_userid', 0)
    if user_id == 0:
        data['status'] = 0    # 0  代表未登录   1原密码输入不正确     2  新密码和原密码一致
        data['msg'] = '登录状态失效，请重新登录！'
        return HttpResponse(json.dumps(data))

    # 筛选用户信息
    userinfo = users.objects.filter(id=user_id).first()
    if userinfo == None:  # 该情况基本不会出现
        data['status'] = 0     # 0  代表未登录   1原密码输入不正确     2  新密码和原密码一致
        data['msg'] = '用户不存在！'
        return HttpResponse(json.dumps(data))

    # 验证输入的原密码是否正确
    md = hashlib.md5()
    md.update(userpass.encode('utf-8'))  # 加密
    md5_password = md.hexdigest()
    print(md5_password)
    print(userinfo.password)
    if userinfo.password!=md5_password:
        data['status'] = 1     # 0  代表未登录   1原密码输入不正确     2  新密码和原密码一致
        data['msg'] = '原始密码输入有误！'
        return HttpResponse(json.dumps(data))

    #验证新密码是否与原密码箱等
    if userpass == usernewpass:
        data['status'] = 2
        data['msg'] = '新密码和原密码一致！'
        return HttpResponse(json.dumps(data))

    data['status'] = 3
    data['msg'] = '修改密码成功！'
    return HttpResponse(json.dumps(data))

#修改密码的提交
def do_edit_pass(request):
    # 获取注册的用户名和密码
    user_id = request.session.get('U_userid', 0)
    passwd = request.POST.get('password',0)

    # 对密码进行加密
    md = hashlib.md5()
    md.update(passwd.encode('utf-8'))
    md5_password = md.hexdigest()

    # 向数据库提交数据
    result=users.objects.filter(id=user_id).update(password=md5_password)
    if result:
        request.session.clear()
        return HttpResponseRedirect('/user/login')
    else:return HttpResponse('更改失败！请联系管理员。')
'''
    #两种更新数据库的方法
    username=request.session.get('U_username')
    userObj=users()
    userObj.id=user_id
    userObj.username=username
    userObj.password=md5_password
    userObj.save()
    return HttpResponseRedirect('/user/login')
'''

# 验证码
def verify_code(request):
    #1、创建画板（画布） 2、创建画笔   3、画相应的图片   4、保存图片并退出
    img_color= (random.randint(0,255),random.randint(0,150),random.randint(0,255))
    img = Image.new('RGB',(100,25),img_color)
    draw=ImageDraw.Draw(img)
    str='ABC1D2EF3GH4IJ5KL6MN70PQ8RS9TUV0WXYZ'  #候选字符串
    font=ImageFont.truetype('simkai.ttf',25)   #字体字号
    x,y=0,0
    font_str=''
    #生成验证码
    for i in range(0,5):
        #字体颜色
        one_str=str[random.randint(0,len(str)-1)]
        font_str+=one_str
        color=(random.randint(0,255),random.randint(150,255),random.randint(0,255))
        #横纵坐标   内容   颜色   字号
        draw.text((x,y),one_str,fill=color,font=font)
        x+=20

    #画干扰点
    for z in range(0,200):
        point_color=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        draw.point((random.randint(0,100),random.randint(0,25)),fill=point_color)

    #画干扰线
    draw.line(((20,15),(90,18)),fill=(0,0,0))
    draw.line(((15,5),(100,22)),fill=(0,0,0))

    io=BytesIO()
    img.save(io,'png')   #保存图片
    request.session['verify_code']=font_str.lower()    #将验证码存入session用于验证用户输入
    return HttpResponse(io.getvalue(),'image/png')


#检查验证码是否正确
def checked_code(request):
    verify_code=request.POST.get('verify_code','')
    verify_code=verify_code.lower()
    loca_code=request.session['verify_code']
    # print(verify_code)
    # print(loca_code)
    data={}
    # 判断验证码
    if len(verify_code) != 5:
        data['msg'] = '验证码错误'
        data['status'] = 0
        return HttpResponse(json.dumps(data))
    if  loca_code !=verify_code:
        data['msg']='验证码错误！'
        data['status']=0
        return HttpResponse(json.dumps(data))
    else:
        data['msg']='验证码正确！'
        data['status']=1
        return HttpResponse(json.dumps(data))


#发送消息--邮件
def send_msg(request):
    uid=request.session.get('temp_uid',0)
    user_info=users.objects.filter(id=uid).first()
    host='http://127.0.0.1:8000'
    address=reverse('user:activate_email')
    parameter={}
    parameter['Uid']=uid
    parameter['t']=int(time.time())

    url_list=[]
    for key,val in parameter.items():
        url_list.append(str(key)+ '=' + str(val))

    url_param="&".join(url_list)
    url=host+address+"?"+url_param

    md=hashlib.md5()
    md.update(url_param.encode('utf-8'))
    token=md.hexdigest()
    url+='&token='+token

    num=send_mail('标题','邮件内容','水果商城<18737307883@163.com>',[user_info.email],html_message='您已注册成功，请点击：<a href="%s">登录验证</a>进行验证！'%(url))
    return HttpResponse('发送成功!')

# 激活账号
def activate_email(request):
    id=request.GET.get('Uid','0')
    t=request.GET.get('t')
    token=request.GET.get('token')

    now_time=time.time()

    str='Uid='+id+'&t=' +t

    md=hashlib.md5()
    md.update(str.encode('utf-8'))
    new_token=md.hexdigest()

    print(token,new_token)

    if token!=new_token:
        return HttpResponse('链接无效！')

    if now_time-int(t)>(60*30):
        return HttpResponse('链接已失效，请重新获取！')

    bool=users.objects.filter(id=id).update(is_activate=1)

    if bool:
        return message()
    else:
        return HttpResponse('激活失败！')

# 注册成功的提示页面
def message(msg='操作成功!'):
    return render_to_response('user/message.html', {'msg': msg})



def test_pay(request):
    """
        设置配置，包括支付宝网关地址、app_id、应用私钥、支付宝公钥等，其他配置值可以查看AlipayClientConfig的定义。
        """
    pass


#支付宝回调页面
def return_url(request):
    # print(request.POST)
    # print(request.GET)
    order_code=request.GET.get('out_trade_no')
    bool=orders.objects.filter(order_code=order_code).update(pay_status=1,pay_time=datetime.datetime.now())
    return message("支付成功！<a href='%s'>继续购物</a>" % ("/"))