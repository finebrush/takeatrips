from rest_framework import viewsets, filters
from imageupload_rest.serializers import UploadedImageSerializer
from imageupload.models import UploadedImage


# ViewSet for our UploadedImage Model
# Gets all images from database and serializes them using UploadedImageSerializer
# class UploadedImagesViewSet(viewsets.ModelViewSet):
#     queryset = UploadedImage.objects.all()
#     serializer_class = UploadedImageSerializer

from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status

from .serializers import UploadedImageSerializer

class UploadedImagesViewSet(viewsets.ModelViewSet):
    queryset = UploadedImage.objects.all()
    serializer_class = UploadedImageSerializer

class FileView(APIView):
  parser_classes = (MultiPartParser, FormParser)

  def get(self, request, format=None):
        snippets = UploadedImage.objects.all()
        serializer = UploadedImageSerializer(snippets, many=True)
        return Response(serializer.data)

  def post(self, request, *args, **kwargs):
    file_serializer = UploadedImageSerializer(data=request.data)
    if file_serializer.is_valid():
      file_serializer.save()
      return Response(file_serializer.data, status=status.HTTP_201_CREATED)
    else:
      return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
