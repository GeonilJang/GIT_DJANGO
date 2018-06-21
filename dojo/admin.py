from django.contrib import admin

from .models import Post

# Register your models here.
##데이블 정의에 대한 정보를 담고 있는 post

"""
모델의 정보를 어드민 페이지에 등록해준다는 의미 입니다.
만약에 모델클래스는 post로 만들지 안도 다른 이름으로 만들었다면
그거를 import 하여 등록 시켜 주면됩니다.
근데 그거느 한마드로 무었을 말하는 거냐면 ----> 데이터 베이스 정보를 등록해주는 것이라고 생각하면된다
"""

"""
어드민페이지 커스텀 하기


방법1)
class PostAdmin(admin.ModelAdmin):
    list_display =['id','title','create_at','update_at']

#커스텀한 어드민 클래스를 2번째의 인자로 넣어서 사용할 수 있다.
admin.site.register(Post, PostAdmin)
"""
# class PostAdmin(admin.ModelAdmin):
#     list_display =['title','content','create_at','update_at']
# admin.site.register(Post, PostAdmin)



"""
장식자를 이용한 방법
방법2)
"""
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','content','create_at','update_at']
