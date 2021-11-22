# Generated by Django 3.2.9 on 2021-11-22 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address_book', '0007_auto_20211122_2130'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='home_number',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(max_length=50, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='address',
            name='street',
            field=models.CharField(max_length=50, verbose_name='Street'),
        ),
        migrations.AlterUniqueTogether(
            name='address',
            unique_together={('country', 'city', 'street', 'home_number')},
        ),
    ]
