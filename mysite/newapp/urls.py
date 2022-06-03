from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', main, name='mail_article'),
    path('acrticles', acrticles, name='acrticles'),
    path('acrticles/archive', archive, name='archive'),
    path('users', users, name='users'),
    path('article/<int:article_id>/', id_num, name='id_article'),
    path('article/<int:article_id>/archive/', id_num_archive, name='id_article_archive'),
    path('article/<int:article_id>/<slug:slug_text>/', slug_text_response, name='id_article_archive_slug'),
    path('users/<int:user_id>/', user_id_num, name='id_user'),
    re_path('/^(\+?\d+)?\s*(\(\d+\))?[\s-]*([\d-]*)$/', regex),
    # path('<int:article_id>/<slug:name>', article, name='article_name'),
]
