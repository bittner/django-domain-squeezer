django-domain-squeezer
======================

*Squeeze some juice out of your parked domains! They deserve it.*

django-domain-squeezer turns your unused domain into a fully working website.
Incoming traffic is always converted into valid content displayed as a web
page.  You decide whether you want to display ads or content from publicly
available sources that match the incoming search request, or manually added
links to (external) sites.  Adding analytics services is easy too.

Note that it's your job to create a beautiful theme for your website project!
If you don't know where to start type `responsive design website templates`_
into your search engine slot, or better, ask the next best web design agency.


.. _responsive design website templates:
    https://duckduckgo.com/?q=responsive+design+website+templates

Setup
-----

#. Create a Django project::

    $ django-admin createproject revivemydomain

#. Install django-domain-squeezer::

    $ pip install django-domain-squeezer

#. Add ``domain_squeezer`` and its dependencies to your project's
   ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        # ...
        'django.contrib.sites',
        'analytical',
        'domain_squeezer',
    )

#. Append the django-domain-squeezer ``urls`` to your project's ``urls.py``::

    urlpatterns = [
        # ...
        url(r'^', include('domain_squeezer.urls')),
    ]

#. Add a ``SQUEEZER_SITEMAP`` setting to your project's ``settings.py`` file.
   See the Settings_ section below for details.

#. Adapt your templates, and beautify the new home for your domain.

Settings
--------

The following values are available in your project settings file.

:SQUEEZER_SITEMAP:
   Dictionary for content displayed in the website footer.
   ``words`` are used to generate random links that make up a sitemap.
   ``links`` are a manual selection of your favorite links to external sites.

   **Default:** ::

      {
          'words': [
              'Home', 'domains', 'monetize',
          ],
          'links': [
              ('GitHub', 'https://github.com/bittner/django-domain-squeezer'),
              ('PyPI', 'https://pypi.python.org/pypi/django-domain-squeezer'),
          ],
      }

:SQUEEZER_URL_MAX_WORDS:
   Maximum length of URL path in words (maximum words evaluated in URL).

   **Default:** ``20``

:Analytics Services:
   See the `documentation of django-analytical`_ on how to set up the service
   of your choice.


.. _documentation of django-analytical:
    https://pythonhosted.org/django-analytical/

Site Settings And Several Domains
---------------------------------

You may want to set the name and domain of your website in the database using
the *Sites* model in the Django Admin.

Optionally, if you want to run several sites with a single Django project you
can do so with Django's `sites framework`_.


.. _sites framework: https://docs.djangoproject.com/en/1.8/ref/contrib/sites/
