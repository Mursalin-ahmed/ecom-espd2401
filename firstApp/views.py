from django.shortcuts import render, redirect
from .models import Profile


# Create your views here.


def Home(request):
    prof = Profile.objects.filter(name__icontains='a')
    print(prof)
    return render(request, 'home.html', locals())
