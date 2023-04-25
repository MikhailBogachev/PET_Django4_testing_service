from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Count

from .models import SetOfTests, Test, Answer, UserResults


def index(request):
    """Главная страница со списком тестов."""
    set_of_tests = SetOfTests.objects.annotate(count_tests=Count('set__id'))
    context = {
        'sets': set_of_tests,
    }
    return render(request, 'questionnaire/index.html', context=context)


@login_required
def set_page(request, set_id):
    """Страница с отдельным тестом и его описанием."""
    set = get_object_or_404(SetOfTests, pk=set_id)
    cnt_tests = Test.objects.filter(set_of_tests=set).count()
    result = UserResults.objects.get_or_create(
        user=request.user,
        set_of_tests=set
    )[0].count_correct_answer

    context = {
        'set': set,
        'result': result,
        'cnt_tests': cnt_tests
    }
    return render(request, 'questionnaire/set_page.html', context=context)


@login_required
def passing_test(request, num_set, num_test):
    """Страница с вопросом теста и вариантами ответов."""
    if num_test == 1:
        obj = UserResults.objects.get(
            user=request.user,
            set_of_tests=num_set
        )
        obj.count_correct_answer = 0
        obj.save()

    has_multiple_answers = SetOfTests.objects.get(pk=num_set).has_multiple_answers
    question = Test.objects.get(
        set_of_tests=num_set,
        number=num_test
    )
    answers = Answer.objects.filter(test=question)

    context = {
        'question': question,
        'num_set': num_set,
        'answers': answers,
        'has_multiple_answers': has_multiple_answers,
    }
    return render(
        request,
        'questionnaire/passing_test.html',
        context=context
    )


@login_required
def get_answer(request, num_set, num_test):
    """Механизм принятия ответа и проверки его корректности"""
    tests = Test.objects.filter(set_of_tests=num_set)
    cnt_tests = tests.count()
    test = tests.get(number=num_test)
    cnt_right_answers = Answer.objects.filter(test=test, is_rigth=True).count()

    try:
        answers = Answer.objects.filter(pk__in=request.POST.getlist('choice'))
    except (KeyError, Answer.DoesNotExist):
        return passing_test(request, num_set, num_test)
    else:
        if (answers.filter(is_rigth=True).count()
            == answers.count()
            == cnt_right_answers
        ):
            tmp_res = UserResults.objects.get(
                user=request.user,
                set_of_tests=num_set
            )
            tmp_res.count_correct_answer += 1
            tmp_res.save()

    if num_test < cnt_tests:
        return redirect(f'/passing_test/{num_set}/{num_test + 1}/')
    return redirect(f'/show_result/{num_set}/')


@login_required
def show_result(request, num_set):
    """Страница с результатами теста"""
    cnt_correct_answers = UserResults.objects.get(
        user=request.user,
        set_of_tests=num_set
    ).count_correct_answer
    cnt_test = Test.objects.filter(
        set_of_tests=num_set
    ).aggregate(Count('id'))['id__count']
    result = round(cnt_correct_answers / cnt_test, 2) * 100

    context = {
        'count_correct_answers': cnt_correct_answers,
        'count_tests': cnt_test,
        'result': result
    }
    return render(request, 'questionnaire/result.html', context=context)
