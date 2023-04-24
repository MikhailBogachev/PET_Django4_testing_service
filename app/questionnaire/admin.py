from django.contrib import admin

from .models import SetOfTests, Test, Answer


class AnswerInline(admin.StackedInline):
    model = Answer
    extra = 5

class TestAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]
    list_display = ('number', 'text', 'set_of_tests',)
    list_editable = ('number',)
    list_display_links = ('set_of_tests',)

admin.site.register(SetOfTests)
admin.site.register(Test, TestAdmin)
