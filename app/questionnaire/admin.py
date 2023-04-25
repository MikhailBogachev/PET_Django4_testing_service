from django.contrib import admin

from .models import SetOfTests, Test, Answer


class AnswerInline(admin.StackedInline):
    model = Answer
    extra = 5

class TestAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]
    list_display = ('number', 'text', 'set_of_tests',)
    list_editable = ('number',)
    list_display_links = ('text',)

class SetOfTestsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'has_multiple_answers')
    list_editable = ('has_multiple_answers',)

admin.site.register(SetOfTests, SetOfTestsAdmin)
admin.site.register(Test, TestAdmin)
