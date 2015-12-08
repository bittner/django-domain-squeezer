"""
URL path mapping for our Django app.
"""
from django.conf.urls import url

from . import views
from .settings import URL_MAX_WORDS

urlpatterns = [
    url(r'^$', views.index, name='squeezer-index'),
]

# match every single element in URL path
for times in range(1, URL_MAX_WORDS + 1):
    pattern = r'^' + (r'([^/]+)/+' * times) + r'$'
    urlpatterns.append(
        url(pattern, views.path, name='squeezer-path')
    )
