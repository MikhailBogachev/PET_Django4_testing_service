from django.contrib import admin

from .models import SetOfTests, Test, Answer


admin.site.register(SetOfTests)
admin.site.register(Test)
admin.site.register(Answer)
