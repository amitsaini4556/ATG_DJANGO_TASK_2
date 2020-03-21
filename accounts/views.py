from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth

import random
import operator
operators=['+','-','*','/']
operators_dict = {
    "+": operator.add,
    "-": operator.sub,
    "/": operator.truediv,
    "*": operator.mul
}







def login(request):
    if request.method=='POST':
        user=auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
             return render(request,'accounts/login.html',{'error':'Username or Password is incorrect.'})
    else:
       return render(request,'accounts/login.html')
def signup(request):
    if request.method=='POST':
        ans=request.POST['captcha']
        value0=request.POST['randomlist0']
        value1=request.POST['randomlist1']
        op=request.POST['op']
        number1=int(value0)
        number2=int(value1)
        result=operators_dict[op](number1,number2)
        int_ans=int(ans)
        if int_ans==result:
            if len(request.POST['password1'])>=8:
                if request.POST['password1']==request.POST['password2']:
                    try:
                        user=User.objects.get(username=request.POST['username'])
                        randomlist = random.sample(range(0, 9), 2)
                        x = random.choice(operators)
                        context3={
                        'error':'username has already been taken',
                        'x':x,
                        'randomlist': randomlist,
                        }
                        return render(request,'accounts/signup.html',context3)
                    except User.DoesNotExist:
                        user=User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                        auth.login(request,user)
                        return redirect('home')
                else:
                    randomlist = random.sample(range(0, 9), 2)
                    x = random.choice(operators)
                    context1 = {
                    'error':'Password must match!!!',
                    'x':x,
                    'randomlist': randomlist,
                    }
                    return render(request,'accounts/signup.html',context1,)

            else:
                randomlist = random.sample(range(0, 9), 2)
                x = random.choice(operators)
                context5={
                'error':'Length of Password must be 8 charachter!!',
                'x':x,
                'randomlist': randomlist,
                }
                return render(request,'accounts/signup.html',context5)

        else:
            randomlist = random.sample(range(0, 9), 2)
            x = random.choice(operators)
            context2={
            'error':'enter the captcha correctly',
            'x':x,
            'randomlist': randomlist,
            }
            return render(request,'accounts/signup.html',context2)
    else:
                    randomlist = random.sample(range(0, 9), 2)
                    x = random.choice(operators)
                    context4={
                    'x':x,
                    'randomlist': randomlist,
                    }
                    return render(request,'accounts/signup.html',context4)

def logout(request):
    if request.method=='POST':
        auth.logout(request)
        return redirect('login')
