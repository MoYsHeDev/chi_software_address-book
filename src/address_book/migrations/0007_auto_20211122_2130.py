# Generated by Django 3.2.9 on 2021-11-22 21:30

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('address_book', '0006_person_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('city', models.CharField(max_length=50, verbose_name='Name')),
                ('street', models.CharField(max_length=50, verbose_name='Name')),
            ],
            options={
                'unique_together': {('country', 'city', 'street')},
            },
        ),
        migrations.AddField(
            model_name='person',
            name='address',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.RESTRICT, related_name='address', to='address_book.address'),
        ),
    ]
