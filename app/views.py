from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
from app.models import User, Produce, Record
from django.contrib import auth
from django.contrib.auth.models import User
import datetime
from django.db.models import Max
from django.http import JsonResponse


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user:
            request.session['username'] = username
            auth.login(request, user)
            return redirect('/lists/')
        # else:
        #     return HttpResponse('用户名密码错误')
    return render(request, 'login.html')


def reg(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.create_user(username=username, password=password)
        return redirect('/login/')
    return render(request, 'reg.html')


def logout(request):
    auth.logout(request)
    return redirect('/login/')


from django.views.decorators.cache import cache_page  # 导入设置缓存的装饰器
@cache_page(60 * 3)  # 注意 60*3 是缓存时间为3分钟，(3)3秒，如果更换了设置，千万记得更新url，否则会使用原来设置的过期时间，和原来的缓存；
def lists(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    else:
        plist = Produce.objects.all()
    return render(request, 'lists.html', locals())


def listss(request):
    result = Record.objects.values('p_id').annotate(price=Max('r_price'))
    ps1 = Produce.objects.filter(pid=1).first()
    ps2 = Produce.objects.filter(pid=2).first()
    ps3 = Produce.objects.filter(pid=3).first()
    ps4 = Produce.objects.filter(pid=4).first()
    p1_result = Record.objects.filter(p_id=1)
    p1 = p1_result.aggregate(Max('r_price'))['r_price__max']
    person1 = Record.objects.filter(p_id=1, r_price=p1).first()
    # list1.append(person1)
    p2_result = Record.objects.filter(p_id=2)
    p2 = p2_result.aggregate(Max('r_price'))['r_price__max']
    person2 = Record.objects.filter(p_id=2, r_price=p2).first()
    # list2.append(person2)
    p3_result = Record.objects.filter(p_id=3)
    p3 = p3_result.aggregate(Max('r_price'))['r_price__max']
    person3 = Record.objects.filter(p_id=3, r_price=p3).first()
    # list3.append(person3)
    p4_result = Record.objects.filter(p_id=4)
    p4 = p4_result.aggregate(Max('r_price'))['r_price__max']
    person4 = Record.objects.filter(p_id=4, r_price=p4).first()
    result = Record.objects.values('p_id').annotate(price=Max('r_price'))
    return render(request, 'listss.html', locals())


from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def p_detail(request, pid):
    p = Produce.objects.get(pid=pid)
    r_list = Record.objects.filter(p_id=p.pid)
    r_max = r_list.aggregate(Max('r_price'))['r_price__max']
    if request.method == 'POST':
        username = request.session['username']
        r_time = datetime.datetime.now()
        r_price = request.POST.get('r_price')
        r_person = username
        record = Record.objects.create(p_id=p.pid, r_time=r_time, r_price=r_price, r_person=r_person)
    return render(request, 'p_detail.html', locals())

# def ajax(request):
#     r_price = request.POST.get('r_price')
#     if r_price >= r_max:
#         data = 'yes'
#     else:
#         data = '不能低于最高竞拍价'
#     return JsonResponse({'key': data})

