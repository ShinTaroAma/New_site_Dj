from django.shortcuts import render


def main(request):
    return render(request, 'index.html')


def id_num(request, article_id, slug_text=''):
    status = article_id % 2 == 0
    if slug_text:
        return render(request, 'slug.html', {"show_id": article_id, "status": status, "slug_text": slug_text})
    return render(request, 'static.html', {"show_id": article_id, "status": status})

