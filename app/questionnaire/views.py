from django.shortcuts import render, HttpResponse

from .models import SetOfTests, Test, Answer


def index(request):
    set_of_tests = SetOfTests.objects.all()
    context = {
        'sets': set_of_tests,
    }
    return render(request, 'questionnaire/index.html', context=context)
