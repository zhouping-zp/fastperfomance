from django.urls import path, re_path
from rest_framework.routers import SimpleRouter, DefaultRouter
# from projects.views import
from system import views
# 定义路由对象
router = SimpleRouter()
# 使用路由对象.register()方法进行注册
# a.第一个参数指定路由的前缀，r‘子应用小写’   第二个参数指定视图集，不需要调用.as_view()
router.register(r'system', views.SystemViewSets)

urlpatterns = [
    # path('projects/', views.ProjectViewSets.as_view({'get': 'list', 'post': 'create'})),
    # path('projects/<int:pk>/',
    #      views.ProjectViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

]
# 使用路由对象.urls属性来获取自动生成的路由条码，往往为列表，需要将这个列表添加至urlpatterns
urlpatterns += router.urls
