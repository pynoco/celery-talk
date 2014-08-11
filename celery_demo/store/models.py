from django.db import models

from sorl.thumbnail import get_thumbnail, delete

# Create your models here.
class ImageStore(models.Model):
    image = models.ImageField(upload_to='images')

    def make_thumbnails(self):
        """ Generate thumbnail sizes that
        are used throughout the site.  When a new size is used
        add it here so that it can be generated on upload.
        """
        get_thumbnail(self.image, '75x75', crop="center", quality=50)
        print("Thumbnail Made")
        get_thumbnail(self.image, '1024x650', quality=100)
        print("Thumbnail Made")
        get_thumbnail(self.image, '240x165')
        print("Thumbnail Made")
        get_thumbnail(self.image, '240x161', crop="center", quality=75)
        print("Thumbnail Made")
        get_thumbnail(self.image, '300x220')
        print("Thumbnail Made")
        get_thumbnail(self.image, '300x300')
