# Generated by Django 4.2 on 2023-04-07 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foundationcommittee',
            name='qualification',
            field=models.CharField(choices=[('PhD', 'PhD.'), ('Masters', 'Masters'), ('Bachelors', 'Bachelors Degree/HND'), ('NCE', 'NCE'), ('Diploma', 'Diploma'), ('SSCE', 'SSCE')], max_length=200),
        ),
    ]