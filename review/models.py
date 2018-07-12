from django.db import models

title = models.CharField(max_length=100, verbose_name='제목', help_text="포스팅 제목을 입력해 주세요. 최대 100글자.")

# Create your models here.
class Review(models.Model):
    manager = models.CharField(max_length=10, verbose_name="담당자", help_text="검수자", blank=True )
    shopid = models.CharField(max_length=20, verbose_name="가맹점 ID", help_text="가맹점 ID", blank=True)
    shopname = models.CharField(max_length=20, verbose_name="가맹점명", help_text="가맹점명", blank=True)
    shopurl = models.CharField(max_length=100, verbose_name="가맹점URL", help_text="가맹점URL", blank=True)
    hosting = models.CharField(max_length=20, verbose_name="호스팅사", help_text="호스팅사", blank=True)
    server = models.TextField(max_length=100, verbose_name="네임서버", help_text="네임서버", blank=True)
    checklogin = models.TextField(max_length=100, verbose_name="비회원구매", help_text="비회원구매", blank=True, default="1.바로구매하기:가능<br>2.장바구니:가능")
    checkcont = models.TextField(max_length=100, verbose_name="사이트구조", help_text="사이트구조", blank=True, default="1.상세페이지:특이사항없음<br> 2.장바구니:특이사항없음<br> 3.옵션기능:특이사항없음")
    opinion = models.TextField(verbose_name="검토의견", help_text="검토의견", blank=True)
    fitness = models.CharField(max_length=10, verbose_name="적합도", help_text="적합도", blank=True, default="상/중/하")
    dateregi = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.shopname
