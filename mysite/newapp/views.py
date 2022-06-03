from django.shortcuts import render
from django.http import HttpResponse


def main(request):
    return HttpResponse("Hey! It's your main view!!")


def acrticles(request):
    return HttpResponse("It's another acrticles!!")


def archive(request):
    return HttpResponse('There will be a list with articles')


def users(request):
    return HttpResponse('This is List of users')


def id_num(request, article_id):
    return HttpResponse(f'Its {article_id} article')


def id_num_archive(request, article_id):
    return HttpResponse(f'Its {article_id} article')


def slug_text_response(request, article_id, slug_text=''):
    return HttpResponse("This is an article #{}. {}".format(article_id, "Name of this article is {}".format(
        slug_text) if slug_text else "This is unnamed article"))


def user_id_num(request, user_id):
    return HttpResponse(f'Its {user_id} user id')


def regex(request):
    return HttpResponse("Regex")
