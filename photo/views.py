from django.shortcuts import render

from .models import Photo
# Create your views here.

def photo_list(request):
    photos = Photo.objects.all()
    return render(request,'photo/list.html',{'photos':photos})
    
