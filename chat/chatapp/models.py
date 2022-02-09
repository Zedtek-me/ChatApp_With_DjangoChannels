from distutils.command.upload import upload
from operator import mod
from django.db import models
from django.contrib.auth.models import User
import datetime
from PIL import Image

# profile of the auth_user_mode objects
class UserProfile(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    image= models.ImageField( default='default.jpg', upload_to='profile_pics/')
    
    def __str__(self):
        return self.user.username

    def save(self):
        super().save()
        img= Image.open(self.image.path)
        if img.height > 500 or img.width >500:
            size= (500, 500)
            img.thumbnail(size)
            img.save(self.image.path)
    
# the messages table to be used for storing messages in a room per sender
class Messages(models.Model):
    room_messages=models.CharField(max_length=50000000000000)
    sender=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.room_messages

# getting all of the images uploaded by the user for display in a template.
class UploadedImage(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    image= models.ImageField(default='deafult.jpg', upload_to='Uploaded_Image/')
    date= models.DateField('uploaded on', auto_now_add=True)

    def __str__(self):
        return '%s uploaded the images here' % self.user.username

    def save(self):
        super().save()
        img= Image.open(self.image.path)
        if img.height > 500 or img.width >500:
            size= (500, 500)
            img.thumbnail(size)
            img.save(self.image.path)

    # a meta class within for ordering the images based on the recent
    class Meta:
        get_latest_by= 'date'


# table for the posts made by a user
class Post(models.Model):
    owner= models.ForeignKey(User, on_delete=models.CASCADE)
    content= models.CharField(max_length=200000000000000000, default= f"Posted on {datetime.datetime.now()}", null=True)
    image= models.ImageField(default='default.jpg', null=True, upload_to='Post_images/')
    date= models.DateField(auto_now_add=True)

    def __str__(self):
        return self.owner


    def __str__(self):
        return self.content
        
    def save(self):
        super().save()
        img= Image.open(self.image.path)
        if img.height > 500 or img.width >500:
            size= (500, 500)
            img.thumbnail(size)
            img.save(self.image.path)

    class Meta:
        get_latest_by= 'date'