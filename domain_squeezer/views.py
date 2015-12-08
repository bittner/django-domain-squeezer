"""
View logic of our Django app.
"""
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse_lazy


def index(request):
    return render_to_response('domain_squeezer/index.html')


def path(request, *args):
    words = []
    for word in args:
        word = word.strip().lower()
        if word and word not in words:
            words.append(word)

    breadcrumb = []
    for i, word in enumerate(words):
        url_path = reverse_lazy('squeezer-path', args=words[:i + 1])
        breadcrumb.append((word, url_path))

    context = {
        'words': words,
        'breadcrumb': breadcrumb,
    }
    return render_to_response('domain_squeezer/path.html', context)
