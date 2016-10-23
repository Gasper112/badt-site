from django.shortcuts import render
from .models import Post
from django.utils import timezone

def home(request):
    return render(request, 'home.html',{})

def post_list(request):
    posts = Post.objects.all().order_by('publish_date')
    return render(request, 'post_list.html',{'post':posts})

def test_list(request):
    return render(request, 'test_list.html',{})




