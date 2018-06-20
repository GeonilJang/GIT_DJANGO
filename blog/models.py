from django.db import models


import re
from django.forms import ValidationError

# Create your models here.
"""
데이터 베이스 모델링 하기

validators 함수를 지정할 수 있다.
"""

#경도 위로를 표현 하기위한 정규식과 그 함수
def lnglat_validator(value):
    if not re.match(r'^([+-]?\d+\.?\d*),([+-]?\d+\.?\d*)$',value):
        raise ValidationError('Invalid Lnglat Typeo')


class Post(models.Model):
    STATUS_CHOICES =(
        ('d','Draft'),
        ('p','Published'),
        ('w','Withdrawn'),
    )

    author =models.CharField(max_length=20)
    # title = models.CharField(max_length=100,
    #                          choices=(
    #                             ('제목1','레이블1'),
    #                             ('제목2','레이블2'),
    #                             ('제목3','레이블3'),
    #                             ('제목4','레이블3'),
    #                          ))
    title = models.CharField(max_length=100, verbose_name='제목', help_text="포스팅 제목을 입력해 주세요. 최대 100글자.")
    content = models.TextField(verbose_name='내용')

    tag_set = models.ManyToManyField('Tag') #릴레이션을 할때는 테그 문자열로 넣어 준다

    lnglat = models.CharField(max_length=50, help_text='경도/위도 포맷 으로', blank=True, validators=[lnglat_validator])
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    create_at = models.DateTimeField(auto_now_add=True) #생성되는 그 순가의 값일 넣는다.
    update_at = models.DateTimeField(auto_now=True) #업데이트 되는 그 시간을 계속 기록한다.

    class Meta:
        ordering = ['-id'] #해당필드 오름 차수 / -내림차수

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post)
    author = models.CharField(max_length=20)
    message = models.TextField()
    create_at = models.DateField(auto_now_add = True)
    update_at = models.DateField(auto_now=True)


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name #이름으로 보여주기



















#
# class Images(models.Model):
#     author =models.CharField(max_length=20)
