# Generated by Django 3.1 on 2020-08-28 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Login', '0003_auto_20200829_0106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(default='media/profile.png', upload_to='profile_pics'),
        ),
    ]
