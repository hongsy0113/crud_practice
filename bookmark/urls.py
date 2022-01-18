from django.urls import path
from . import views

# 템플릿엥서 app name을 바로바로 url 타고 가기 쉽게 하기 위해서
# app 이 여러개 일 떄
app_name = "bookmark"

urlpatterns = [
    path('', views.list, name="list"),
    path('<int:pk>/', views.cate_detail, name="cate_detail"),
    path('cate_new/', views.cate_new, name='cate_new'),
    path('<int:pk>/cafe_edit/', views.cate_edit, name='cate_edit'),
    path('<int:pk>/cate_delete/', views.cate_delete, name='cate_delete'),
    path('mark_new/', views.mark_new, name='mark_new'),
    path('<int:pk>/mark_edit/', views.mark_edit, name='mark_edit'),
    path('<int:pk>/mark_delete/', views.mark_delete, name='mark_delete'),
]
