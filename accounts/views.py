from django.shortcuts import render
from .models import Profile
# Create your views here.

qs = Profile.objects.all()

# @login_required
def profile(request):
    return render(request,"accounts/profile.html")
