import os
import uuid

from PIL import Image
from django.db import models
from django.conf import settings


def scramble_uploaded_filename(instance, filename):
    """
    Scramble / uglify the filename of the uploaded file, but keep the files extension (e.g., .jpg or .png)
    :param instance:
    :param filename:
    :return:
    """
    extension = filename.split(".")[-1]
    return "{}.{}".format(uuid.uuid4(), extension)


def create_thumbnail(input_image, thumbnail_size=(256, 256)):
    """
    Create a thumbnail of an existing image
    :param input_image:
    :param thumbnail_size:
    :return:
    """
    # make sure an image has been set
    if not input_image or input_image == "":
        return

    # open image
    image = Image.open(input_image)

    # use PILs thumbnail method; use anti aliasing to make the scaled picture look good
    image.thumbnail(thumbnail_size, Image.ANTIALIAS)

    # parse the filename and scramble it
    filename = scramble_uploaded_filename(None, os.path.basename(input_image.name))
    arrdata = filename.split(".")
    # extension is in the last element, pop it
    extension = arrdata.pop()
    basename = "".join(arrdata)
    # add _thumb to the filename
    new_filename = basename + "_thumb." + extension

    # save the image in MEDIA_ROOT and return the filename
    image.save(os.path.join(settings.MEDIA_ROOT, new_filename))

    return new_filename

class UploadedImage(models.Model):

    bs_thename = models.CharField("location name", max_length=255, default="Unknown Picture")
    bs_theimg = models.ImageField("Uploaded image", upload_to="%Y/%m/%d", null=True, blank=True)

    # thumbnail
    #thumbnail = models.ImageField("Thumbnail of uploaded image", blank=True)

    # title and description
    bs_title = models.CharField("Title of intro image", max_length=255, default="Unknown Picture")
    bs_writer = models.CharField("writer of intro image", max_length=255, default="Unknown Picture")

    def __str__(self):
        return self.bs_thename
    #어떻게 쓰이는지 모름
    @property
    def sub_images(self):
        return self.image_set.all()

class SubImage(models.Model):
    uploadedimage = models.ForeignKey(UploadedImage, related_name='sub_images', on_delete=models.CASCADE, null=True, blank=True)
    path = models.ImageField("Uploaded image", upload_to="%Y/%m/%d", null=True, blank=True)

    #def save(self, force_insert=False, force_update=False, using=None, update_fields=None):

        # generate and set thumbnail or none
        #self.thumbnail = create_thumbnail(self.image)

        # Check if a pk has been set, meaning that we are not creating a new image, but updateing an existing one
        #if self.pk:
        #    force_update = True

        # force update as we just changed something
        #super(UploadedImage, self).save(force_update=force_update)
