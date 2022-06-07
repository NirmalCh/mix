from contextlib import redirect_stderr
import email
from urllib import request
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from yaml import serialize
from sahakari_app.models import Account_info
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .serializers import Account_InfoSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt


from django.core.paginator import Paginator
# Create your views here.


class Account_InfoList(APIView):
    def get(self,request):
        account_info= Account_info.objects.all()
        serializer=Account_InfoSerializer(account_info,many=True)
        return Response(serializer.data)

    def post(self,request):
        pass


def home(request):
    
    return render(request, 'sahakari/home.html')

@login_required()
def account(request):
    if request.method == 'GET':
        return render(request, 'Account/account.html')
    else:
        account_no = request.POST['Account_no']
        account = Account_info.objects.get(account_number=account_no)
        
        return render(request, 'Account/account_info.html',context={'account':account})

@csrf_exempt
def register(request):
    if request.method == 'GET':
    
        return render(request, 'Auth/register.html')
    else:
        
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        address = request.POST['address']
        phone = request.POST['phone']
        dob = request.POST['dob']
        citizen_no = request.POST['citizen_no']
        form = Account_info(request.POST, request.FILES)
        if form.is_valid():
            instance = Account_info(images_fields=request.FILES['img'])
            instance.save()
        user=User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
        Account_info.objects.create(user=user, address=address, phone=phone, dob=dob, citizenship_no=citizen_no)
        return HttpResponse("done")
        

def signin(request):
    if request.method == 'GET':
        return render(request, 'Auth/login.html')
    else:
        username=request.POST['username']
        password = request.POST['password']
        user= authenticate(username=username, password=password)
        if user is not None:
            login(request, user)

            next_url = request.GET.get('next')

            if next_url is None:
                return redirect('home')
            else:
                return redirect(next_url)
        else:
            return redirect('signin')


def signout(request):
    logout(request)
    return redirect('signin')


def general_profile(request):
    user= User.objects.get(id=request.user.id)
    account= Account_info.objects.get(user=user)
    return render(request, 'Personal/general.html', context={'account':account})

def general_edit(request):
    user= User.objects.get(id=request.user.id)
    account= Account_info.objects.get(user=user)
    if request.method == 'GET':
        return render (request, 'Auth/general_edit.html' ,context={'account':account})
    else:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        address = request.POST['address']
        phone = request.POST['phone']
        dob = request.POST['dob']
        citizenship_no = request.POST['citizen_no']
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        account.address = address
        account.phone = phone
        account.dob = dob
        account.citizenship_no = citizenship_no
        user.save()
        account.save()
        return redirect('general')

def privacy(request):
    userinfo = User.objects.get(id = request.user.id)
   
    if request.method == 'GET':
        return render(request, 'Auth/privacy.html')

    else:
        username = request.POST['username']
        email = request.POST['email']
        username1 = request.POST['username1']
        n_password = request.POST['n_password']
       
        password = request.POST['password1']
        user= authenticate(username=username, password=password)
        if user is not None:
           user.username = username1
           user.email = email
           user.password = n_password
           user.save()
           return redirect('home')
            
        else:
            return redirect('privacy')


def personal_account(request):
    user= User.objects.get(id=request.user.id)
    account= Account_info.objects.get(user=user)
    return render(request, 'Account/personal_account.html', context={'account':account})