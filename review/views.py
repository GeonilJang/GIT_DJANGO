from django.shortcuts import render
from django.http import HttpResponse
from .models import Review

from django.http import Http404

from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def review_list(request):

    reviews = Review.objects.all()

    page = request.GET.get('page', 1)
    paginator = Paginator(reviews, 10)
    try:
        reviews = paginator.page(page)
        if len(reviews) < 10:
            currentPage = len(Review.objects.all())
        else:
            currentPage = len(reviews)*int(page)
    except PageNotAnInteger:
        reviews = paginator.page(1)
    except EmptyPage:
        reviews = paginator.page(paginator.num_pages)




    return render(request, 'review/review_list.html',{
        "reviews":reviews,
        "currentPage":currentPage
    })



def update_for_review(value):
    regidata = value.split("\t")
    dic  = {
        "manager":regidata[0],
        "shopid":regidata[1],
        "shopname":regidata[2],
        "shopurl":regidata[3]
    }
    print(dic)
    Review.objects.create(manager=dic['manager'],shopid=dic['shopid'],shopname=dic["shopname"], shopurl=dic["shopurl"])
        # queryset.update(manager=dic['manager'],shopid=dic['shopid'],shopname=dic["shopname"], shopurl=dic["shopurl"])

    return "dic"

def review_regi(request):
    if request.method == "POST":
        print(request.POST['inputdata'])
        regiInputDate = request.POST['inputdata']
        regiarr = regiInputDate.split("\n")
        for regiElement in regiarr:
            regidata = update_for_review(regiElement)

            print(regidata)



    else:
        raise Http404()
    return HttpResponse("""
                        Hello world
                        """)
