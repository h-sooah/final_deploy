from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User   # User모델을 import했어요!
from django.contrib import auth  # auth라는 모듈도 import합니다. 서버로 넘어온 유저 데이터를 처리하는 역할을 할거에요!
from .models import Blog
from .models import Sell_list
from .models import Buy_list
from django.utils import timezone
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator

def home(request):
    return render(request, 'blog/index.html')

def userlogin(request):   # userlogin으로 꼭 안하셔도 되고 login등등으로 마음껏 하셔도 됩니다!
    if request.method == 'POST':     # 앞에서 설명한대로 유저 정보는 노출되면 안되기 때문에 POST 메서드를 사용해 유저가 입력한 로그인 정보를 서버로 보내줬어요!
        username = request.POST['username']  # request에 담겨온 데이터 중 username의 데이터를 username변수에 담아줬어요!
        password = request.POST['password']  # 마찬가지로 password데이터를 password변수에 담아줍니다
        user = auth.authenticate(request, username = username, password = password) 
					# auth모듈에 내장된 authenticate메서드는 request(요청)을 인자로 받고, 우리가 사용자로부터 받은 username,password를 User모델 데이터들 중에서 일치하는 유저를 가져다 user변수에 담아줍니다.
        if user is not None:  # 그래서 사용자가 보낸 데이터가 User테이블의 데이터와 일치하는게 있으면, 그걸 user변수에 담아줄거고, 그 user변수가 None이 아닐 때, 즉 유저가 있을 때를 여기서 처리합니다.
            auth.login(request, user)  # auth모듈의 login메서드를 통해 위에서 가져온 user를 로그인 처리합니다.
            return redirect('home') # 그리고 로그인이 정상적으로 되면 index페이지로 리다이렉트 시켜주죠!
        else :
            return render(request, 'blog/userlogin.html', {'error':'username or password is incorrect'}) # 만약에 위에서 user변수에 아무 유저도 담기지 않았다면, 즉 로그인 정보가 유효하지 않으면 화면을 넘기지 않고 메시지를 띄워줍니다.
    else :  # 요청이 POST방식이 아니라면, 즉 로그인 페이지에 들어오는 get방식의 요청이 있을 때
        return render(request, 'blog/userlogin.html') # 로그인 화면을 띄워주는 html을 렌더링 해줍니다.
    return render(request, 'blog/userlogin.html')


def signup(request): # 회원가입 함수입니다.
    if request.method == 'POST':   # POST방식일 때, 즉 서버로 데이터가 넘겨졌을 때(사용자가 회원가입 정보를 입력하고 가입하기를 눌렀을 때) 아래 함수를 실행합니다.
        if request.POST['password1'] == request.POST['password2']: # 우리가 '비밀번호'와 '비밀번호 확인' 두 개의 데이터를 받아 이 두 항목이 일치할 때 회원가입을 진행시켜줄거에요!
            user = User.objects.create_user(username = request.POST['username'], password = request.POST['password1'])
						# 비밀번호 확인이 되면, 넘어온 회원가입 데이터를 가지고 User모델에 유저 데이터를 생성해줍니다.
            auth.login(request, user) # 그리고 회원가입이 성공적으로 수행된 후에 자동으로 로그인을 한번 해줍니다.
            return redirect('home')
    return render(request, 'blog/signup.html') # Post방식이 아닌 get방식일 경우 회원가입창을 띄워줍니다.

def logout(request):
    auth.logout(request)
    return redirect('home')

def notice(request):
    blogs = Blog.objects
    return render(request, 'blog/notice.html', {'blogs': blogs})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog_detail})

def sell(request):
    sells = Sell_list.objects
    sell_list = Sell_list.objects.all()
    paginator = Paginator(sell_list, 6)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'blog/sell.html', {'sells': sells, 'posts':posts})

def buy(requset):
    buys = Buy_list.objects
    buy_list = Buy_list.objects.all()
    paginator = Paginator(buy_list, 6)
    page = requset.GET.get('page')
    posts = paginator.get_page(page)
    return render(requset, 'blog/buy.html', {'buys': buys, 'posts':posts})

def buy_detail(request, buy_id):
    buy_detail = get_object_or_404(Buy_list, pk=buy_id)
    return render(request, 'blog/buy_detail.html', {'buy': buy_detail})

def sell_detail(request, sell_id):
    sell_detail = get_object_or_404(Sell_list, pk=sell_id)
    return render(request, 'blog/sell_detail.html', {'sell': sell_detail})

def buy_form(request):
    return render(request, 'blog/buy_form.html')

def buying(request):
    blog_buy = Buy_list()
    blog_buy.buy_name = request.GET['buy_name']
    blog_buy.amount = request.GET['amount']
    blog_buy.price = request.GET['price']
    blog_buy.body = request.GET['body']
    blog_buy.pub_date = timezone.datetime.now()
    blog_buy.request_country = request.GET['request_country']
    blog_buy.end_date = request.GET['end_date']
    blog_buy.size = request.GET['size']
    blog_buy.save()
    return redirect('buy')

def sell_form(request):
    return render(request, 'blog/sell_form.html')

def selling(request):
    blog_sell = Sell_list()
    blog_sell.name = request.GET['name']
    blog_sell.phone_number = request.GET['phone_number']
    blog_sell.account_number = request.GET['account_number']
    blog_sell.body = request.GET['body']
    blog_sell.pub_date = timezone.datetime.now()
    blog_sell.method = request.GET['method']
    blog_sell.country = request.GET['country']
    blog_sell.start_date = request.GET['start_date']
    blog_sell.end_date = request.GET['end_date']
    return redirect('sell')
    