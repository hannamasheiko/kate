from django.conf.urls import include,url
from . import views
from django.contrib import admin

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'', include('blog.urls')),

]
