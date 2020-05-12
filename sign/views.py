from django.shortcuts import render_to_response
from django.shortcuts import render,get_object_or_404
from django.http.response import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from sign.models import Event,Guest
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

# Create your views here.
def index(request):
    # return render_to_response('index.html')
    return render(request,'index.html')

def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username = username,password = password)
        if user is not None:
            auth.login(request,user)
            # 将session记录到浏览器
            request.session['user'] = username
            response = HttpResponseRedirect('/event_manage/')
            # #添加浏览器cookie
            # response.set_cookie('user',username,3600)
            return response
        else:
            return render(request,'index.html',{'error':'username or password error!'})
    else:
        return render(request,'index.html',{'error':'username or password error1!'})

#发布会管理
@login_required
def event_manage(request):

    event_list = Event.objects.all()
    # #读取浏览器cookie
    # username =request.COOKIES.get('user','')

    #读取浏览器session
    username = request.session.get('user','')
    return render(request,'event_manage.html',{'user':username,'events':event_list})

#按发布会名称搜索
@login_required
def search_event_name(request):
    username = request.session.get('user')
    search_event_name =request.GET.get('name')
    event_list = Event.objects.filter(name__contains=search_event_name)
    return render(request,'event_manage.html',{'user':username,'events':event_list})

#嘉宾管理
@login_required
def guest_manage(request):

    guest_list = Guest.objects.all()
    # #读取浏览器cookie
    # username =request.COOKIES.get('user','')

    #读取浏览器session
    username = request.session.get('user','')
    paginator = Paginator(guest_list,10)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
    # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
    # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    return render(request, 'guest_manage.html', {'user':username, 'guests':contacts})

#按嘉宾名称搜索
@login_required
def search_guest_name(request):
    username = request.session.get('user')
    search_guest_name = request.GET.get('realname')
    guest_list = Guest.objects.filter(realname__contains = search_guest_name)
    # paginator = Paginator(guest_list,10)
    # page = request.GET.get('page')
    # try:
    #     contacts = paginator.page(page)
    # except PageNotAnInteger:
    # # If page is not an integer, deliver first page.
    #     contacts = paginator.page(1)
    # except EmptyPage:
    # # If page is out of range (e.g. 9999), deliver last page of results.
    #     contacts = paginator.page(paginator.num_pages)
    return render(request, 'guest_manage.html', {'user':username, 'guests':guest_list})

#签到页面
@login_required
def sign_index(request,event_id):
    event = get_object_or_404(Event,id=event_id)
    return render(request,'sign_index.html',{'event':event})

#签到动作
@login_required
def sign_index_action(request,event_id):
    event = get_object_or_404(Event,id=event_id)
    phone = request.POST.get('phone')
    result = Guest.objects.filter(phone=phone)
    if not result :
        return render(request,'sign_index.html',{'event':event,'hint':'phone error'})
    result = Guest.objects.filter(phone=phone,event_id=event_id)
    if not result :
        return render(request,'sign_index.html',{'event':event,'hint':'event id or phone error'})
    result = Guest.objects.get(phone=phone,event_id=event_id)
    if result.sign:
        return  render(request,'sign_index.html',{'event':event,'hint':'user has sign in '})
    else:
        Guest.objects.filter(phone=phone,event_id=event_id).update(sign=1)
        return render(request,'sign_index.html',{'event':event,'hint':'sign in success!','guest': result})

#退出登录
@login_required
def logout(request):
    auth.logout(request)
    response = HttpResponseRedirect('/index/')
    return response


