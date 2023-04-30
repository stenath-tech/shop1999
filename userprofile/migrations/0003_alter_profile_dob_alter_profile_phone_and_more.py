# Generated by Django 4.1.7 on 2023-04-17 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_remove_profile_firstname_remove_profile_lastname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='dob',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='pix',
            field=models.ImageField(default='avatar.jpg', upload_to='Profile'),
        ),
    ]
