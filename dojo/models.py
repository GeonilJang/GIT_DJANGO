from django.db import models

# Create your modelss here.

##모델을 만든다 -> 즉 데이터 베이스테이블을 하나 만든다 이다!!!!
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
