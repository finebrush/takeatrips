from rest_framework import serializers
from imageupload.models import UploadedImage, SubImage

# Serializer for UploadedImage Model
# serializes pk and image

class SubImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubImage
        fields = ( 'uploadedimage', 'path',)

class UploadedImageSerializer(serializers.ModelSerializer):
    sub_images = SubImageSerializer(many=True)
    class Meta:
        model = UploadedImage
        fields = ('pk', 'bs_thename', 'bs_theimg', 'bs_title', 'bs_writer','sub_images')

    def create(self,validated_data):
        print(validated_data)
        sub_images = validated_data.pop('sub_images') #sub_images는 비어있음 -> []
        uploadedimage = UploadedImage.objects.create(**validated_data)
        images_data = self.context.get('view').request.FILES

        count_data = 0 #bs_theimg 를 포함시키지 않기 위해서 첫번째는 그냥 넘긴다.
        for image_data in images_data.values():
            if count_data == 0:
                count_data = 1
            else:
                SubImage.objects.create(uploadedimage=uploadedimage, path=image_data)
        return uploadedimage
