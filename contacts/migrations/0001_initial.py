# Generated by Django 4.2 on 2023-04-07 22:04

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Phone number')),
                ('subject', models.CharField(choices=[('Enquiry', 'Enquiry'), ('Donations', 'Donations'), ('Support', 'Support')], max_length=20)),
                ('message', models.TextField()),
                ('status', models.CharField(choices=[('attended', 'Attended'), ('ignored', 'Ignored'), ('pending', 'Pending')], default='pending', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
