from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Count

from .models import SetOfTests, Test, Answer, UserResults


def index(request):
    set_of_tests = SetOfTests.objects.all()
    context = {
        'sets': set_of_tests,
    }
    return render(request, 'questionnaire/index.html', context=context)


@login_required
def set_page(request, set_id):
    set = get_object_or_404(SetOfTests, pk=set_id)
    result = UserResults.objects.get_or_create(user=request.user, set_of_tests=set)
    context = {
        'set': set,
        'result': result
    }
    return render(request, 'questionnaire/set_page.html', context=context)


@login_required
def passing_test(request, num_set, num_test):
    set = SetOfTests.objects.get(pk=num_set)
    if num_test == 1:
        obj = UserResults.objects.get(user=request.user, set_of_tests=num_set)
        obj.count_correct_answer = 0
        obj.save()
    question = Test.objects.get(set_of_tests=num_set, number=num_test)
    answers = Answer.objects.filter(test=question)
    context = {
        'question': question,
        'set': set,
        'answers': answers,
    }
    return render(request, 'questionnaire/passing_test.html', context=context)

@login_required
def get_answer(request, num_set, num_test):
    set = SetOfTests.objects.get(pk=num_set)
    cnt_test = Test.objects.filter(set_of_tests=num_set).aggregate(Count('id'))['id__count']
    try:
        answer = Answer.objects.get(pk=request.POST['choice'])
    except (KeyError, Answer.DoesNotExist):
        return passing_test(request, num_set, num_test)
    else:
        print(answer.is_rigth)
        if answer.is_rigth:
            tmp_res = UserResults.objects.get(user=request.user, set_of_tests=set)
            tmp_res.count_correct_answer += 1
            tmp_res.save()
    if num_test < cnt_test:
        return redirect(f'/passing_test/{num_set}/{num_test + 1}/')
    return redirect(f'/show_result/{num_set}/')

@login_required
def show_result(request, num_set):
    cnt_correct_answers = UserResults.objects.get(user=request.user, set_of_tests=num_set).count_correct_answer
    cnt_test = Test.objects.filter(set_of_tests=num_set).aggregate(Count('id'))['id__count']
    result = round(cnt_correct_answers / cnt_test, 2) * 100
    context = {
        'count_correct_answers': cnt_correct_answers,
        'count_tests': cnt_test,
        'result': result
    }
    return render(request, 'questionnaire/result.html', context=context)
