
from django.shortcuts import render

# Create your views here.

# import time
#
# from django.shortcuts import render, redirect
# from django.http import JsonResponse
# from django.views import View
#
# #from .forms import PhotoForm
# from imageupload.models import UploadedImage
#
#
# class BasicUploadView(View):
#     def get(self, request):
#         photos_list = UploadedImage.objects.all()
#         return render(self.request, 'photos/basic_upload/index.html', {'photos': photos_list})
#
#     def post(self, request):
#         form = PhotoForm(self.request.POST, self.request.FILES)
#         if form.is_valid():
#             UploadedImage = form.save()
#             data = {'is_valid': True, 'name': photo.file.name, 'url': photo.file.url}
#         else:
#             data = {'is_valid': False}
#         return JsonResponse(data)
