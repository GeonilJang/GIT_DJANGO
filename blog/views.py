#뷰를 만드는 곳이다
from django.shortcuts import render, get_object_or_404

from django.http import Http404
from django.db.models import Q
from django.http import HttpResponse
from .models import Post

# Create your views here.

#( 1-1 )이 설정한 함수를 프로젝트 밑에 있는 urls.py에 등록해줘야 한다.


def post_list(request):
    #select
    qs = Post.objects.all()
    q = request.GET.get('q','') #q 파라미터로 넘겨주는 파라미터 값
    if q:
        qs = qs.filter(Q(title__icontains=q)) | qs.filter(Q(content__icontains=q))| qs.filter(Q(author__icontains=q))


    return render(request, 'blog/post_list.html',{
        'post_list':qs, #3번째의 인자로 사전형 데이터를 넘겨 줄 수 있다
        'q':q,
    })

def post_detail(request, id):
    # try:
    #     post = Post.objects.get(id=id)
    # except Post.DoesNotExist:
    #     raise Http404
    """
    위 4줄과 똑같은 코드이다.
    """
    post= get_object_or_404(Post, id=id)

    return render(request, 'blog/post_detail.html',{
        'post':post
    })




def test(request, name):
    return HttpResponse(name)
