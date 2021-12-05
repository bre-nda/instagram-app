from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.
class Profile(models.Model):
    profile_photo = CloudinaryField('image')
    bio = models.TextField()

    def update_profile(self):
        self.save()

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

class Image(models.Model):
    image=CloudinaryField('image')
    image_name = models.CharField(max_length=50)
    image_caption = models.TextField()
    posted_on = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)