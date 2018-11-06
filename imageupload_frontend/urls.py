from django.conf.urls import url, include
from django.views.generic.base import RedirectView
from django.views.generic import TemplateView

app_name = 'imageupload_frontend'

# Redirect any request that goes into here to static/index.html
urlpatterns = [
    #url(r'^$', RedirectView.as_view(url='static/base.html', permanent=False), name='index')
    url(r'^$', TemplateView.as_view(template_name='base.html'), name='base'),
    url(r'^basic_info/$', TemplateView.as_view(template_name='basic_info.html'), name='basic_info'),
    url(r'^travel_info/$', TemplateView.as_view(template_name='travel_info.html'), name='travel_info'),
    url(r'^travelcurator/$', TemplateView.as_view(template_name='travelcurator.html'), name='travelcurator'),
    url(r'^travelplan/$', TemplateView.as_view(template_name='travelplan.html'), name='travelplan'),
]
