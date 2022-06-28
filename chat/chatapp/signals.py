from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import UserProfile, UploadedImage
from django.dispatch import receiver
import os
# signal for creating a profile for a newly added user
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        profile= UserProfile(user= instance)
        profile.save()


# signal for getting all uploaded images by the profile table of the user

@receiver(post_save, sender=UserProfile)
def user_uploads(sender, instance, created, update_fields, **kwargs):
    if created:
        upload= UploadedImage(user=instance.user, image=instance.image)
        upload.save()
    elif update_fields:
        upload= UploadedImage(**update_fields)
        upload.save()