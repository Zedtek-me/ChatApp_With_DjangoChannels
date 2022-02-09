from django.contrib import admin
from .models import Messages, UserProfile, UploadedImage,Post
# Register your models here.

admin.site.register([UserProfile,Messages, UploadedImage,Post])