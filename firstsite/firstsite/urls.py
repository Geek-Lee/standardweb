"""firstsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from firstapp.views import index, detail, detail_comment#从view层引入函数index

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index', index, name='index'),#url(‘url地址’，函数名，查找方便名)
    url(r'^detail/(?P<page_num>\d+)$', detail, name='detail'),
    url(r'^detail/(?P<page_num>\d+)/comment$', detail_comment, name='comment'),
]
