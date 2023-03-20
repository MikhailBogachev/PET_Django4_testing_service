from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import SetOfTests, Test, Answer
from .forms import AnswerForm


def index(request):
    set_of_tests = SetOfTests.objects.all()
    context = {
        'sets': set_of_tests,
    }
    return render(request, 'questionnaire/index.html', context=context)


def set_page(request, set_id):
    set = get_object_or_404(SetOfTests, pk=set_id)
    context = {
        'set': set
    }
    return render(request, 'questionnaire/set_page.html', context=context)


# @login_required
def passing_test(request, num_set, num_test):
    set = SetOfTests.objects.get(pk=num_set)
    question = Test.objects.get(set_of_tests=num_set, number=num_test)
    answers = Answer.objects.filter(test=question)
    next_page = num_test + 1
    context = {
        'question': question,
        'set': set,
        'answers': answers,
        'next_page': next_page
    }
    return render(request, 'questionnaire/passing_test.html', context=context)
