from django.shortcuts import render,get_object_or_404
from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect
from.form import Signup,Login,Adam
from.models import Post



#Home
def home(request):
    posts=Post.objects.all()
    return render(request,'blog/home.html',{'posts':posts})


#About
def about(request):
    return render(request,'blog/about.html')

#contact
def contact(request):
    return render(request,'blog/contact.html')

#Dashboard
def dashboard(request):
    if request.user.is_authenticated:
        posts=Post.objects.all()
        user=request.user
        full_name=user.get_full_name()
        return render(request,'blog/dashboard.html',{'posts':posts,'full':full_name})
    else:
        return HttpResponseRedirect('/login/')

#signup
def signup(request):
    if request.method=="POST":
        fm=Signup(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm=Signup()
    return render(request,'blog/signup.html',{'form':fm})

#login
def ulogin(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            fm=Login(request=request,data=request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data['username']
                upass=fm.cleaned_data['password']
                user=authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    return HttpResponseRedirect('/dashboard/')
        else:
            fm=Login()
        return render(request,'blog/login.html',{'form':fm})
    else:
        return HttpResponseRedirect('/dashboard/')

#logout
def ulogout(request):
    logout(request)
    
    return HttpResponseRedirect('/')


#Addpost 
def add_post(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            fm=Adam(request.POST,request.FILES)
            if fm.is_valid():
                fm.save()
                fm=Adam()
        else:
            fm=Adam()
        return render(request,'blog/addpost.html' ,{'form':fm})
    else:
        return HttpResponseRedirect('/login/')
    
def update(request,id):
    if request.user.is_authenticated:
        if request.method=='POST':
            pi=Post.objects.get(pk=id)
            fm=Adam(request.POST,instance=pi)
            if fm.is_valid():
                fm.save()
        else:
            pi=Post.objects.get(pk=id)
            fm=Adam(instance=pi)
        return render (request,'blog/update.html',{'form':fm})
    else:
        return HttpResponseRedirect('/login/')
    
def deleted(request,id):
    if request.user.is_authenticated:
        if request.method=='POST':
            pi=Post.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')


def details(request,id):
    if request.user.is_authenticated:
       obj=get_object_or_404(Post,id=id)
       return render(request,'blog/detail.html',{'obj':obj})
    else:
        return HttpResponseRedirect('/login/')
    
    