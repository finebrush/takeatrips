from django.conf.urls import url, include
from rest_framework import routers
from imageupload_rest.viewsets import UploadedImagesViewSet, FileView

# initiate router and register all endpoints
router = routers.DefaultRouter()
router.register('images', UploadedImagesViewSet, 'images')

# Wire up our API with our urls
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^upload/$', FileView.as_view(), name='file-upload'),
]
