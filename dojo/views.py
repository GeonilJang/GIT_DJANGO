from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
import os
from django.conf import settings

# Create your views here.

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
