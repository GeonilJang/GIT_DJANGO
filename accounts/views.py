from django.shortcuts import render
from .models import Profile
# Create your views here.

qs = Profile.objects.all()

def profile(request):
    return render(request, 'accounts/profile.html',{
        "profiles":qs
    })
