"""
View logic of our Django app.
"""
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse

from .settings import SITEMAP


def default_context():
    external_links = SITEMAP['links']
    internal_links = []

    for element in SITEMAP['words']:
        # TODO: randomize path construction (by day)
        url_path = reverse('squeezer-path', args=[element.lower()])
        internal_links.append((element, url_path))

    return {
        'sitemap': internal_links,
        'links': external_links,
    }


def index(request):
    return render_to_response('domain_squeezer/index.html', default_context())


def path(request, *args):
    words = []
    for word in args:
        word = word.strip().lower()
        if word and word not in words:
            words.append(word)

    breadcrumb = []
    for i, word in enumerate(words):
        url_path = reverse('squeezer-path', args=words[:i + 1])
        breadcrumb.append((word, url_path))

    context = default_context()
    context['words'] = words
    context['breadcrumb'] = breadcrumb

    return render_to_response('domain_squeezer/path.html', context)
