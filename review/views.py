from django.shortcuts import render
from django.http import HttpResponse
from .models import Review

# Create your views here.
def review_list(request):
    reviews = Review.objects.all()
    return render(request, 'review/review_list.html',{
        "reviews":reviews
    })
