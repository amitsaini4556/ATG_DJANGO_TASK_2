from django.shortcuts import render,redirect,get_object_or_404
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Product
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import render,redirect



@login_required(login_url='/accounts/signup')
def home(request):
    product=Product.objects.all().filter(hunter=request.user)
    return render(request,'products/home.html',{'products':product})
@login_required(login_url='/accounts/signup')
def create(request):
    if request.method=='POST':
        if  request.FILES['image'] and request.POST['body']:
            product=Product()
            product.image=request.FILES['image']
            product.body=request.POST['body']
            product.hunter=request.user
            product_strr='Public'
            if product_strr==request.POST['mode']:
                product.post_mode='Public'
            else:
                product.post_mode='Private'
            product.save()
            return redirect('/products/' + str(product.id))
        else:
            return render(request,'products/create.html',{'error':'All fields are required.'})
    else:
       return render(request,'products/create.html')
def detail(request,product_id):
    product=get_object_or_404(Product,pk=product_id)
    return render(request,'products/detail.html' ,{'product':product})



@login_required(login_url='/accounts/signup')
def search(request):
    if request.method=='POST':
        try:
            user=User.objects.get(username=request.POST['search'])
            product=Product.objects.filter(post_mode__icontains='Public').filter(hunter=user)
            return render(request,'products/search.html',{'product':product})
        except User.DoesNotExist:
                product=Product.objects.all().filter(hunter=request.user)
                return render(request,'products/home.html',{'error':'User Does Not Exist!','products':product})
