# Generated by Django 3.2.9 on 2022-01-29 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0015_alter_uploadedimage_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadedimage',
            name='image',
            field=models.ImageField(default='user.userprofile.image.path', upload_to='All_images/'),
        ),
    ]