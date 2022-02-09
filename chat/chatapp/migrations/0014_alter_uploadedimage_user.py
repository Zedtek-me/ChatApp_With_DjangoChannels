# Generated by Django 3.2.9 on 2022-01-29 22:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chatapp', '0013_rename_images_uploadedimage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadedimage',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
