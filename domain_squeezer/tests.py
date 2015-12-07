"""
Tests for this Django app.
"""
from django.test.utils import override_settings


@override_settings(SQUEEZER_SITEMAP={
    'words': ['Home', 'One', 'Two', 'Three'],
    'links': [('Google', 'https://google.com/search?q=squeezer'),
              ('Bing', 'https://bing.com/search?q=squeezer')],
})
def test_sitemap():
    pass
