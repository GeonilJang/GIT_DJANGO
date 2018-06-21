from django.shortcuts import render, redirect
from django.http import HttpResponse , JsonResponse
import os
from django.conf import settings
from .forms import PostForm

from .models import Post
# Create your views here.


def post_new(request):
    if (request.method == 'POST'):
        form = PostForm(request.POST, request.FILES)
        if(form.is_valid()): #토큰을 가지고 들어왔다면 !

            """
            - 데이터 베이스에 값을 저장 시키는 방법 -
            방법1)
            post = Post()
            post.title = form.cleaned_data['title']
            post.content = form.cleaned_data['content']
            post.save()
            """

            #방법2)
            """
            post = Post(
                title =form.cleaned_data['title'],
                content = form.cleaned_data['content']
            )
            post.save()
            """

            #방법3)
            """
            post = Post.objects.create(
                title = form.cleaned_data['title'],
                content = form.cleaned_data['content']
            )
            """

            #방법4) 사전형 데이터이기 때문에 가능한 방법
            """
                post = Post.objects.create(**form.cleaned_data)
            """
            """
                그래서 이렇게 구현 할 수 있고~~!! 실제로 사용할떄는 form.py에서 save함수를 만들어서 거기서 불러다 쓰는 방법을 사용한다!!!
            """
            print(form.cleaned_data)
            post = form.save(commit=False) #아래에서 커빗 하고싶어서 !!

            post.ip = request.META['REMOTE_ADDR'] #화면을 통해 입력 받지 않는 데이터를 데이버페이스에 저장하고 싶을때 쓰는방법
            post.save()
            return redirect('/dojo/')

    else:
        form = PostForm()
    return render(request, 'dojo/post_form.html',{
        'form':form,
    })




















#urls에 등록해주 변수 . 인자를 받을 수 있다. 그 값은 같아야 하는 것으로 보인다
def mysum(request, numbers):
    # return : HttpRequest
    #numners ="1231/12312/3123/13/32/3/21/3/"
    arr = numbers.split("/")
    result = sum(map(int, arr))
    print(arr)
    return HttpResponse(result)


def hello(request, name, age):
    return HttpResponse('안녕하세요 {}. {}입니다.'.format(name,age))


def post_list1(request):
    name ="알룽"
    return HttpResponse("""
                        <h1>장건이 짱 멋쟁이</h1>
                        <p>{name}<p>
                        <p>여러분의 파이썬  & 장고 페이스메이커가 되어드리겠습니다.<p>
                        """.format(name=name))


def post_list2(request):
    name = '건일'
    return render(request, 'dojo/post_list.html',{'name':name})


def post_list3(request):
    return JsonResponse({
        'message': '안녕 하세요',
        'items' : ['파이썬','건일','신애']
    }, json_dumps_params={'ensure_ascii':False})


def excel_download(request):
    # filepath = 'test.xlsx'
    filepath = os.path.join(settings.BASE_DIR, 'test.xlsx')
    filename = os.path.basename(filepath)
    with open(filepath, 'rb') as f:
        response = HttpResponse(f, content_type='application/vnd.ms_excel') #기본 text/html
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)
        return response
