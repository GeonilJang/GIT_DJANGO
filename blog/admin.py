from django.contrib import admin
from django.utils.safestring import mark_safe



from .models import Post , Comment, Tag


# Register your models here.


"""
어드민 페이지 커스텀
방법1)
class PostAdmin(admin.ModelAdmin):
    list_display =['id','title','create_at','update_at']

#커스텀한 어드민 클래스를 2번째의 인자로 넣어서 사용할 수 있다.
admin.site.register(Post, PostAdmin)
"""



"""
방법2)
"""
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','title','content_size','status','create_at','update_at']
    actions = ['make_published','make_draft']

    def content_size(self, post):
        return mark_safe('<strong>{}</strong>글자'.format(len(post.content)))
    content_size.short_description ='글자수'


    def make_draft(self, request, queryset):
        updated_count = queryset.update(status='d')
        self.message_user(request, '{}건의 포스팅을 Draft상태로 변경'.format(updated_count))
    make_draft.short_description = '지정 포스팅을 Draft상태로 변경합니다.'

    def make_published(self, request, queryset):
        updated_count = queryset.update(status='p')
        self.message_user(request, '{}건의 포스팅을 Published상태로 변경'.format(updated_count))
    make_published.short_description = '지정 포스팅을 Published상태로 변경합니다.'

    #content_size.allow_tags = True

    """
    ModelAdmin 옵션들.

    list_display : 목록에 보여질 필드 목록.
    list_display_links : 목록 내에서 링크로 지정할 필드 목록.
    list_editable : 목록상에서 수정할 필드 목록
    list_per_page : 페이지 별로 보여질 최대 갯수
    list_filter : 필터 옵션을 제공할 필드 목록
    """

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['post','author','message']

@admin.register(Tag)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name']
