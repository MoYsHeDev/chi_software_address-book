# Generated by Django 3.2.9 on 2021-11-25 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address_book', '0008_alter_contact_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='profile_pic',
            field=models.ImageField(blank=True, default='media/images/profile_pic1.gif', upload_to='images'),
        ),
    ]
