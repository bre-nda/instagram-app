from django.shortcuts import render
from django.http  import HttpResponse

from instagram.models import Image

# Create your views here.
def welcome(request):
    images = Image.objects.all()
    return render(request, 'home.html', {'images': images})

def search_results(request):
    if 'search' in request.GET and request.GET['search']:
        search_term = request.GET.get('search').lower()
        posts = Image.search_by_name(search_term)
        message = f'{search_term}'

        return render(request, 'search.html', {'success': message, 'posts': posts})
    else:
        message = 'You havent searched for any term'
        return render(request, 'search.html', {'danger': message})

