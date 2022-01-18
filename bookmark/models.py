from unicodedata import category
from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=10)
    desc = models.CharField(max_length=100)

    def __str__(self):
        return "[" + self.name + "]" + self.desc
    # str 함수를 정의하지 않으면 catetory(1) 과 같이 안 예쁘게 뜬다
# str 함수 추가하는 건 테이블을 바꾸는 게 아니므로 migrate 필요 x


class Mark(models.Model):
    name = models.CharField(max_length=20)
    url = models.URLField("Site URL")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return "["+self.category.name+"]" + self.name+" : " + self.url
    # 외래키에선 category에서 어떤 걸 가져올지 명시해줘야 함.
