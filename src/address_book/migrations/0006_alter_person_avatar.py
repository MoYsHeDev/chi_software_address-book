# Generated by Django 3.2.9 on 2021-11-23 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address_book', '0005_alter_phone_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='avatar',
            field=models.ImageField(blank=True, default='profile1.png', null=True, upload_to='staticfiles/images/profile/'),
        ),
    ]
