from django.conf.urls import url, include
from django.views.generic.base import RedirectView
from django.views.generic import TemplateView

# Redirect any request that goes into here to static/index.html
urlpatterns = [
    #url(r'^$', RedirectView.as_view(url='static/base.html', permanent=False), name='index')
    url(r'^$', TemplateView.as_view(template_name='client/cbase.html'), name='cbase'),
]
