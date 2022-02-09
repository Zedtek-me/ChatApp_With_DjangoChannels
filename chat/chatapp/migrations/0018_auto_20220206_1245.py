# Generated by Django 3.2.9 on 2022-02-06 11:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0017_auto_20220206_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='content',
            field=models.CharField(default='Posted on 2022-02-06 12:45:12.407453', max_length=200000000000000000),
        ),
        migrations.AlterField(
            model_name='uploadedimage',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chatapp.userprofile'),
        ),
    ]