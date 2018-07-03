from django.db import models
from django.urls import reverse
# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name='제목', help_text="포스팅 제목을 입력해 주세요. 최대 100글자.")
    content = models.TextField(verbose_name='내용', help_text="내용을 입력해 주세요.")
    user_agent = models.CharField(max_length=200,blank=True)
    ip = models.CharField(max_length=15)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self): #글을 등록하면 자동으로 이동되게 하는 부분
        return reverse('products:product_detail', args=[self.id])
