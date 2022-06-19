from django.shortcuts import redirect, render
from django.contrib import auth
from django.contrib.auth.models import User

# Create your views here.


def login(request):
    # POST 요청시 로그인 처리를 해준다.
    if request.method == 'POST':
        userid = request.POST['username']
        pwd = request.POST['password']
        user = auth.authenticate(request, username=userid, password=pwd)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html')

    # GET 요청시 login form을 갖고있는 login.html을 띄워주는 역할을 함.
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('home')
