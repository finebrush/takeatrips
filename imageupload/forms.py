from .models import UploadedImage

class PhotoForm(forms.ModelForm):
    class Meta:
        model = UploadedImage
        fields = (
            'bs_thename',
            'bs_theimg',
            'bs_title',
            'bs_writer',
            'bs_images'
        )
