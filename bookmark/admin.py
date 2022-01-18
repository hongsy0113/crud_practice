from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Category)
# admin.site.register(Mark)


@admin.register(Mark)
class MarkAdmin(admin.ModelAdmin):
    # 다양한 필드들을 넣을 수 있다.
    # 보이게 할 필드들
    list_display = ['name', 'url', 'category']
    # 디테일 페이지로 넘어갈 수 있게 하는 링크를 넣는다.
    # 안 지정하면 맨 앞에 있는 애만 링크 걸린다
    list_display_links = ['name', 'url','category']
    # search_field 중요. 외래키에 접근할 땐 언더바 두개
    # admin 펭이지에서 검색창이 생긴다

    search_fields = ['name', 'category__name']
