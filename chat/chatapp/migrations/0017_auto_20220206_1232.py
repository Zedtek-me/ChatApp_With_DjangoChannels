# Generated by Django 3.2.9 on 2022-02-06 11:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chatapp', '0016_alter_uploadedimage_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadedimage',
            name='image',
        ),
        migrations.AlterField(
            model_name='uploadedimage',
            name='date',
            field=models.DateField(auto_now_add=True, verbose_name='Uploaded on'),
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(default='Posted on 2022-02-06 12:32:13.986172', max_length=200000000000000000)),
                ('image', models.ImageField(default='', null=True, upload_to='Post_images/')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
