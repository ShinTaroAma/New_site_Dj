from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', main, name='mail_article'),
    path('article/<int:article_id>/', id_num, name='id_article'),
    path('article/<int:article_id>/<slug:slug_text>/', id_num, name='id_article_archive_slug'),

]
