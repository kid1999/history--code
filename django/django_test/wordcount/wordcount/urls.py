
from django.contrib import admin
from django.urls import path
from  . import function  #导入处理方法

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',function.home),  #返回主页
    path('count/',function.count),  #返回结果页

]
