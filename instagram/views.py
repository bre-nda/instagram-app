from django.shortcuts import render
from django.http  import HttpResponse

from instagram.models import Image

# Create your views here.
def welcome(request):
    images = Image.objects.all()
    return render(request, 'home.html', {'images': images})

