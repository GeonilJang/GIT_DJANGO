from django.db import models


#인증을 위해서는 여기 추가
from django import forms
# Create your modelss here.

##모델을 만든다 -> 즉 데이터 베이스테이블을 하나 만든다 이다!!!!''
"""
이거로 모델도 만들고
데이터를 저장할 때도 이거를 사용한다
Post({'title':'geonil','conten':'goengon'}) 이런식으로
"""
#인증을 위해서는 여기 추가
def min_length_3_validator(value):
    if(len(value) < 3):
        raise forms.ValidationError('3글자 이상입력 해줘용')

class Post(models.Model):
    title = models.CharField(max_length=100, validators=[min_length_3_validator])
    content = models.TextField()
    ip = models.CharField(max_length=15)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
