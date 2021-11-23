# Generated by Django 3.2.9 on 2021-11-23 11:03

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('address_book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('city', models.CharField(max_length=50, verbose_name='City')),
                ('street', models.CharField(max_length=50, verbose_name='Street')),
                ('house_number', models.IntegerField(default=None)),
            ],
            options={
                'unique_together': {('country', 'city', 'street', 'house_number')},
            },
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, default=None, max_length=128, region=None, unique=True, verbose_name='Phone')),
            ],
        ),
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(choices=[('FB', 'Facebook'), ('LN', 'Linkedin'), ('IN', 'Instagram'), ('GH', 'GitHub'), ('JN', 'Jinni'), ('TW', 'Twitter'), ('WS', 'WebSite')], default=None, max_length=2)),
                ('url', models.URLField()),
            ],
        ),
        migrations.AddField(
            model_name='person',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default=None, max_length=1),
        ),
        migrations.AlterField(
            model_name='person',
            name='first_name',
            field=models.CharField(max_length=200, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='person',
            name='last_name',
            field=models.CharField(max_length=200, verbose_name='Surname'),
        ),
        migrations.AlterUniqueTogether(
            name='person',
            unique_together={('first_name', 'last_name')},
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='images/profile/')),
                ('address', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, related_name='address', to='address_book.address')),
                ('person', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='person', to='address_book.person')),
                ('phone', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='address_book.phone')),
                ('url', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='address_book.url')),
            ],
        ),
        migrations.AddField(
            model_name='url',
            name='person',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='url', to='address_book.person'),
        ),
        migrations.AddField(
            model_name='phone',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='phone', to='address_book.person'),
        ),
    ]
