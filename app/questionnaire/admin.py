from django.contrib import admin

from .models import SetOfTests, Test, Answer


class TestAdmin(admin.ModelAdmin):
    list_display = ('number', 'text', 'set_of_tests',)
    list_editable = ('number',)
    list_display_links = ('set_of_tests',)

admin.site.register(SetOfTests)
admin.site.register(Test, TestAdmin)
admin.site.register(Answer)
