from django.shortcuts import render

from .models import Bookmarks

# Create your views here.
def index(request):
    context = {
        'bookmarks': Bookmarks.objects.all(),
    }
    return render(request, 'bookmarks/index.html', context)