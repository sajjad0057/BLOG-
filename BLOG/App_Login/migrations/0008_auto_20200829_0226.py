# Generated by Django 3.1 on 2020-08-28 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Login', '0007_auto_20200829_0150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='/profile_pics/profile_pic.png', upload_to='profile_pics'),
        ),
    ]
