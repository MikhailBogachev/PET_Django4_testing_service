from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class SetOfTests(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name='Название теста'
    )
    description = models.TextField(
        verbose_name='Описание теста'
    )


class Test(models.Model):
    number = models.IntegerField()
    text = models.TextField(
        verbose_name='Текст вопроса'
    )
    set_of_tests = models.ForeignKey(
        SetOfTests,
        on_delete=models.CASCADE,
        verbose_name='Набор тестов',
        related_name='set'
    )

    class Meta:
        unique_together = ('number', 'set_of_tests')


class Answer(models.Model):
    text = models.TextField(
        verbose_name='Текст ответа'
    )
    test = models.ForeignKey(
        Test,
        on_delete=models.CASCADE
    )
    is_rigth = models.BooleanField()


class UserResults(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    set_of_tests = models.ForeignKey(
        SetOfTests,
        on_delete=models.CASCADE,
        related_name='results'
    )
    count_correct_answer = models.IntegerField(
        default=0
    )
