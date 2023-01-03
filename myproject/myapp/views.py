from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    context = {
        'name': 'Pawan',
        'age': 21,
        'nationality': 'Pakistani'
    }
    return render(request, 'index.html', context)
