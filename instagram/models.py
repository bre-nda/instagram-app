from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.
class Profile(models.Model):
    profile_photo = CloudinaryField('image')
    bio = models.TextField()

    def __str__(self):
        return self.user.username

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

    def __str__(self):
        return self.image_name

    def delete_image(self):
        self.delete()

    def save_image(self):
        self.save()

    def update_caption(self, new_caption):
        self.image_caption = new_caption
        self.save()

    @classmethod
    def get_images_by_user(cls, user):
        posts = cls.objects.filter(user=user)
        return posts

    @classmethod
    def get_all_comments(self):
        return self.objects.comments.all()
