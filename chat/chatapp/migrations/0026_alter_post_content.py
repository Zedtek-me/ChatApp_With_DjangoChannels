# Generated by Django 3.2.9 on 2022-02-07 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0025_alter_post_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.CharField(default='Posted on 2022-02-07 21:59:32.904976', max_length=200000000000000000),
        ),
    ]
