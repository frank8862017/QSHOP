from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import  GoodsInfo,GoodsType
from manager.models import ManagerMessage,power_roles
from django.conf import  settings
import uuid
from QSHOP.check_power import check_power
# Create your views here.
# 前台首页
def index(request):
    user_id = request.session.get('U_userid', 0)
    list = GoodsInfo.objects.filter()    #查询所有商品
    return render(request,'goods/index.html',{'list':list,'user_id':user_id})

# 显示添加商品页面
@check_power
def goods_add(request):
    goods_type_list=GoodsType.objects.all()
    return render(request,'goods/goods_add.html',{'goods_type_list':goods_type_list})

# 商品添加页面提交操作
def dogoods_add(request):
    # 获取表单信息
    # 商品编号
    goods_num=request.POST['goods_num']
    # 商品名称
    goods_name=request.POST['goods_name']
    # 商品原价
    goods_oprice= request.POST['goods_oprice']
    # 商品现价
    goods_xprice = request.POST['goods_xprice']
    # 库存
    goods_count=request.POST['goods_count']
    # 存储方法
    goods_method=request.POST['goods_method']
    # 商品介绍
    goods_info=request.POST['goods_info']
    # 商品缩略图
    goods_pic=request.FILES.get('goods_pic')

    '''
    hix = ['image/png', 'image/jpg', 'image/gif']
    if goods_pic.content_type not in hix:
        return HttpResponse('图片上传错误！')
    '''

    # 判断上传的图片是否符合要求
    houzhui = str(goods_pic).split('.')[-1]
    houzhui_list = ['png', 'jpg', 'gif']
    if houzhui not in houzhui_list:
        return HttpResponse('图片上传错误！')

    # 给图片重命名（防止重名，django会自动修改名字，也可以不重命名）
    new_file_name = str(uuid.uuid1()) + '.' + houzhui

    # 上传图片  将图片移动到指定目录
    file_path = settings.MEDIA_ROOT + '/media/uploads/' + new_file_name         #保存图片
    save_path = '/media/uploads/' + new_file_name
    with open(file_path, 'wb') as f:
        for content in goods_pic.chunks():
            f.write(content)

    # 配送地址
    goods_address=request.POST['goods_address']
    # 商品内容
    goods_content=request.POST['goods_content']
    # 商品类别
    type_id=request.POST['type_id']

    # 登录验证
    user_id=request.session.get('user_id',0)
    if user_id==0:
        return HttpResponse('请先登录！')

    # 数据插入数据库
    result=GoodsInfo.objects.create(goods_num=goods_num,
                                    goods_name=goods_name,
                                    goods_oprice=goods_oprice,
                                    goods_xprice=goods_xprice,
                                    goods_count=goods_count,
                                    goods_method=goods_method,
                                    goods_info=goods_info,
                                    goods_pic=save_path,
                                    goods_address=goods_address,
                                    goods_content=goods_content,
                                    type01_id=type_id,
                                    manager_id=user_id
                        )
    # 判断是否插入成功
    if result:return HttpResponseRedirect('/goods/goods_list')
    else:return HttpResponse('添加失败')


#   商品列表显示
@check_power
def goods_list(request):
    # 查找所有商品信息
    # list=GoodsInfo.objects.all()
    user_id=request.session.get('user_id',0)
    list=GoodsInfo.objects.filter(manager_id=user_id)
    # list=GoodsInfo.objects.raw('select * from goods_goodstype inner join goods_goodsinfo on goods_goodstype.type_id=goods_goodsinfo.type_id;')
    return render(request,'goods/goods_list.html',{'list':list})


# 删除商品信息
def goods_delete(request,pk):
    try:
        user_id=request.session.get('user_id',0)

        goods=GoodsInfo.objects.get(id=pk)

        # 验证有没有越权操作
        if goods.manager_id !=user_id:
            return HttpResponse('没有操作权限！')
        else:
            goods.delete()
            return HttpResponseRedirect('/goods/goods_list')
    except:return HttpResponse('删除失败，请联系管理员！')


# 编辑商品信息（更新、修改）--显示修改页面
def goods_modify(request,pk):
    user_id=request.session.get('user_id',0)
    goods = GoodsInfo.objects.get(id=pk)
    if goods.manager_id !=user_id:
        return HttpResponse('操作有误！')
    goods_type_list=GoodsType.objects.all()
    return  render(request,'goods/goods_modify.html',{'goods':goods,'goods_type_list':goods_type_list})

# 编辑商品信息（更新、修改）--提交
def dogoods_modify(request):
    # 获取表单信息
    # 商品编号
    goods_num = request.POST['goods_num']
    # 商品名称
    goods_name = request.POST['goods_name']
    # 商品原价
    goods_oprice = request.POST['goods_oprice']
    # 商品现价
    goods_xprice = request.POST['goods_xprice']
    # 库存
    goods_count = request.POST['goods_count']
    # 存储方法
    goods_method = request.POST['goods_method']
    # 商品介绍
    goods_info = request.POST['goods_info']
    # 商品缩略图
    goods_pic=request.FILES.get('goods_pic')

    # 判断图片是否符合格式（另一种方式：判断后缀）
    # hix=['image/png','image/jpg','image/gif']
    # if goods_pic.content_type not in hix:
    #     return HttpResponse('图片上传错误！')

    houzhui=str(goods_pic).split('.')[-1]
    houzhui_list=['png','jpg','gif']
    if houzhui not in houzhui_list:
        return HttpResponse('图片上传错误！')

    # 为图片重命名
    new_file_name=str(uuid.uuid1())+'.'+houzhui

    # 上传图片  将图片移动到指定目录
    file_path=settings.MEDIA_ROOT+'/media/uploads/'+ new_file_name
    save_path='/media/uploads/'+ new_file_name

    with open(file_path,'wb') as f:
        for content in goods_pic.chunks():
            f.write(content)

    # 配送地址
    goods_address = request.POST['goods_address']
    # 商品内容
    goods_content = request.POST['goods_content']
    # 商品id
    id=request.POST['type_id']
    # 数据库操作
    goods=GoodsInfo.objects.filter(id=id)

    user_id=request.session.get('user_id',0)
    # 验证
    if goods[0].manager_id!=user_id:
        return HttpResponse('操作有误！')
    result=goods.update(goods_num=goods_num,
                goods_name=goods_name,
                goods_oprice=goods_oprice,
                goods_xprice=goods_xprice,
                goods_count=goods_count,
                goods_method=goods_method,
                goods_info=goods_info,
                goods_pic=save_path,
                goods_address=goods_address,
                goods_content=goods_content)
    if result:return HttpResponseRedirect('/goods/goods_list')
    else:return HttpResponse('修改！请联系管理员。')


# 开店页面——显示
def openstore(request):
    return render(request,'goods/openstore.html')


# 开店页面——提交
def doopenstore(request):
    # 获取数据
    username=request.POST['username']
    nicheng=request.POST['nicheng']
    shop_name=request.POST['shop_name']
    shop_logo=request.FILES['shop_logo']
    shop_address=request.POST['shop_address']

    # 默认初始密码000000
    # 数据库操作
    result=ManagerMessage.objects.create(username=username,
                                  nicheng=nicheng,
                                  shop_name=shop_name,
                                  shop_logo=shop_logo,
                                  shop_address=shop_address,
                                  userpass='000000')
    if result:
        return  HttpResponseRedirect('/goods/welcome')
    else:return HttpResponse('注册失败！')


# 欢迎页面——显示
def welcome(request):
    return render(request,'goods/welcome.html')


# 前台列表页
def goods_type(request):
    tid=request.GET.get('tid',0)

    if tid==0:
        list=GoodsInfo.objects.filter()  #查询所有商品
    else:
        list=GoodsInfo.objects.filter(type01_id=tid)  #查询所有商品

    # 获取商品分类信息
    type_list=GoodsType.objects.filter()
    return render(request,'goods/goods_type.html',{'list':list,'type_list':type_list})


# 显示商品详情
def goods_details(request):
    id=request.GET.get('gid',0)
    print('id',id)
    if id==0:
        return  HttpResponse('你要看什么？')

    goods=GoodsInfo.objects.filter(id=id).first()

    # 获取其他商品
    other_goods_list=GoodsInfo.objects.filter(type01_id=goods.type01_id)
    print(other_goods_list)
    return render(request,'goods/goods_details.html',{'shop':goods,'other_goods_list':other_goods_list})

# 鲜果页
def fruit(request):
    list=GoodsInfo.objects.filter(type01_id=1)
    return render(request,'goods/index.html',{'list':list})