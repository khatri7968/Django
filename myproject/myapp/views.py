from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature

# Create your views here.
def index(request):

    feature1 = Feature()
    feature1.id = 0
    feature1.name = 'Fast'
    feature1.is_correct = True
    feature1.details = 'Our service is very quick'

    feature2 = Feature()
    feature2.id = 1
    feature2.name = 'You Observe'
    feature2.is_correct = True
    feature2.details = 'We have best teaching staff'

    feature3 = Feature()
    feature3.id = 2
    feature3.name = 'What you get'
    feature3.is_correct = True
    feature3.details = 'One of the best learning plateform in the world'

    feature4 = Feature()
    feature4.id = 3
    feature4.name = 'Our Past Records'
    feature4.is_correct = False
    feature4.details = 'We have many birlliant students which are having 2.5s lac per month and more than that'

    feature5 = Feature()
    feature5.id = 4
    feature5.name = 'Affordable'
    feature5.is_correct = True
    feature5.details = 'Our service is very affordable'

    features = [feature1, feature2, feature3, feature4, feature5]

    for feature in features:
        pass

    return render(request, 'index.html', {'features': features})
def counter(request):
    text = request.POST['text']
    amount_of_words = len(text.split())
    return render(request, 'counter.html', {'amount': amount_of_words})