from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def weather1(request,city,year):
    print(city)
    print(year)
    Quer_dict = request.GET
    a = Quer_dict.get('a')#查询一个结果，键值对，a=1
    b = Quer_dict.getlist('b')#查询多个结果，返回列表，a=[1,10]
    # 创建COOKIE 不建议线上使用
    # response = HttpResponse('ok')
    # response.set_cookie('q1','a1',max_age=86400)
    # response.delete_cookie('q1')
    # print(request.COOKIES.get('q1'))
    return HttpResponse