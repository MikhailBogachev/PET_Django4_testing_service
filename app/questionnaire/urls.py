from django.urls import path

from . import views


app_name = 'questionnaire'
urlpatterns = [
    path(
        '',
        views.index,
        name='index'
    ),
    path(
        'set_page/<int:set_id>/',
        views.set_page,
        name='set_page'
    ),
    path(
        'passing_test/<int:num_set>/<int:num_test>/',
        views.passing_test,
        name='passing_test'
    ),
    path(
        'get_answer/<int:num_set>/<int:num_test>/',
        views.get_answer,
        name='get_answer'
    ),
    path(
        'show_result/<int:num_set>/',
        views.show_result,
        name='show_result'
    ),
]
