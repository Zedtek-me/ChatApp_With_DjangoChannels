# Generated by Django 3.2.9 on 2022-02-08 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0028_auto_20220207_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.CharField(default='Posted on 2022-02-08 14:22:29.184086', max_length=200000000000000000, null=True),
        ),
    ]