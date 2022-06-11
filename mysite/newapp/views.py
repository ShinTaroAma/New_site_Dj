from typing import Any

from django.shortcuts import render
from django.http import HttpResponse


def main(request):
    s = [i for i in range(0, 100)]
    return render(request, 'index.html', {'time_now': s})


def id_num(request, article_id, slug_text=''):
    status = article_id % 2 == 0
    if slug_text:
        return render(request, 'slug.html', {"show_id": article_id, "status": status, "slug_text": slug_text})
    return render(request, 'static.html', {"show_id": article_id, "status": status})

