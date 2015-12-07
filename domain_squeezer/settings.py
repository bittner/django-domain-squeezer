"""
Settings of this Django app.
"""
from django.conf import settings

SITEMAP = getattr(settings, 'SQUEEZER_SITEMAP', {
    'words': [
        'Home', 'domains', 'monetize',
    ],
    'links': [
        ('GitHub', 'https://github.com/bittner/django-domain-squeezer'),
        ('PyPI', 'https://pypi.python.org/pypi/django-domain-squeezer'),
    ],
})

URL_MAX_WORDS = getattr(settings, 'SQUEEZER_URL_MAX_WORDS', 20)
