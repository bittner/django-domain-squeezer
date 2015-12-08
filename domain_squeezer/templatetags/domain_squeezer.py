from django import template
from django.core.urlresolvers import reverse_lazy
from django.contrib.sites.shortcuts import get_current_site

from ..settings import SITEMAP

register = template.Library()


@register.inclusion_tag('domain_squeezer/tags/sitemap.html')
def site_sitemap():
    """Return a list of randomized internal links that look like a sitemap."""
    internal_links = []

    for element in SITEMAP['words']:
        # TODO: randomize path construction (by day)
        url_path = reverse_lazy('squeezer-path', args=[element.lower()])
        internal_links.append((element, url_path))

    return {'sitemap': internal_links}


@register.inclusion_tag('domain_squeezer/tags/links.html')
def site_links():
    """Return a list of external links as defined in the project settings."""
    external_links = SITEMAP['links']

    return {'links': external_links}


@register.simple_tag
def site_name():
    """Website name as stored in the database (Django sites framework)."""
    return get_current_site.name


@register.simple_tag
def site_domain():
    """Website domain as stored in the database (Django sites framework)."""
    return get_current_site.domain
