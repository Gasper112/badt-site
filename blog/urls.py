from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^test/', views.test_list, name ='test_list'),
    url(r'^post/', views.post_list, name ='post_list'),
    url(r'^$', views.home, name = 'home'),
]
