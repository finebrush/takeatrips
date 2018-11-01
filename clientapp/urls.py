from django.conf.urls import url, include
from django.views.generic.base import RedirectView
from django.views.generic import TemplateView

# Redirect any request that goes into here to static/index.html
urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='client/cintro.html'), name='cbase'),
    url(r'^main/$', TemplateView.as_view(template_name='client/cmain.html'), name='cmain'),
]
