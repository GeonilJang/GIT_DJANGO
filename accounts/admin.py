from django.contrib import admin

from .models import Profile
# Register your models here.
from django.utils.safestring import mark_safe


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id','_user','phone_num','address']
#content_size.short_description ='글자수'
    def phone_num(self, post):
        return mark_safe('<strong>{}</strong>'.format(post.phone_number))
    phone_num.short_description ='전화번호'
    def _user(self, post):
        return mark_safe('<strong>{}</strong>'.format(post.user))
    _user.short_description ='아이디'

#
# ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
# ('phone_number', models.CharField(max_length=20)),
# ('address', models.CharField(max_length=50)),
# ('user
