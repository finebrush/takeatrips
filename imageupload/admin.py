from django.contrib import admin
from imageupload.models import UploadedImage, SubImage

# Register the UploadedImage Model for the Admin Page
admin.site.register(UploadedImage)
admin.site.register(SubImage)
