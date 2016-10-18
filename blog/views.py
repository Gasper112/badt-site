from django.shortcuts import render

def home(request):
    return render(request, 'home.html',{})

def post_list(request):
    return render(request, 'post_list.html',{})

def test_list(request):
    return render(request, 'test_list.html',{})


