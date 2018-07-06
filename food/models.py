from django.db import models

# Create your models here.
class Food(models.Model):
    author = models.CharField(max_length=20, verbose_name="작성자")
    title = models.CharField(max_length=100, verbose_name="제목",help_text="제목을 입력해 주세요. 최대 100글자.")
    content = models.TextField(verbose_name="내용")
    photo = models.ImageField(blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('food:food_detail', args=[self.id])
