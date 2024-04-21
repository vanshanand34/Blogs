from django.shortcuts import render
from django.urls import reverse
from .models import Post
# Create your views here.

def index(request):
    posts = Post.objects.all()
    return render(request,'index.html',{'posts':posts})

def mypost(request,pk):
    post = Post.objects.get(pk=pk)
    return render(request,'index.html',{'mypost':post})

    
def create(request):
    if request.method=='POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        mypost = Post.objects.create(title=title,body=content)
        if mypost is not None:
            mypost.save()
            return render(request,'index.html',{'posts':Post.objects.all()})
    return render(request,'create.html')