# Generated by Django 3.1 on 2020-08-28 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Login', '0004_auto_20200829_0115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(upload_to='profile_pics'),
        ),
    ]
