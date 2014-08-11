from django import forms


from store.models import ImageStore

class ImageStoreForm(forms.ModelForm):

    class Meta:
        model = ImageStore
