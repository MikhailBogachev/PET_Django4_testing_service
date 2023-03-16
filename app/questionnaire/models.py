from django.db import models


class SetOfTests(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name='Название теста'
    )
    description = models.TextField(
        verbose_name='Описание теста'
    )


class Test(models.Model):
    text = models.TextField(
        verbose_name='Текст вопроса'
    )
    set_of_tests = models.ForeignKey(
        SetOfTests,
        on_delete=models.CASCADE,
        verbose_name='Набор тестов'
    )


class Answer(models.Model):
    text = models.TextField(
        verbose_name='Текст ответа'
    )
    test = models.ForeignKey(
        Test,
        on_delete=models.CASCADE
    )
    is_rigth = models.BooleanField()
