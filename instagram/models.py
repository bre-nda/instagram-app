from django.db import models
from cloudinary.models import CloudinaryField

class Image(models.Model):
    image = CloudinaryField('image', default='')
    name = models.CharField(max_length = 30,default='')
    caption = models.TextField()
    likes = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)

    
    def __str__(self):
        return self.name
    
    @classmethod
    def search_by_name(cls,search_term):
        images = cls.objects.filter(title__icontains = search_term)
        return images
    
    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()
    
    def update_caption(self, new_caption):
        self.image_caption = new_caption
        self.save()

class Profile(models.Model):
    profile_photo=CloudinaryField('image')
    bio = models.TextField(max_length=500)
