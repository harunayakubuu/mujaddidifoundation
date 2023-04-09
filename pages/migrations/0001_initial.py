# Generated by Django 3.2.16 on 2023-04-09 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoundationCommittee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=6)),
                ('designation', models.CharField(choices=[('CHAIRMAN', 'Chairman')], max_length=20)),
                ('words', models.CharField(max_length=100)),
                ('display_picture', models.ImageField(help_text='Width: 400px, Height: 400px', upload_to='pictures/foundation_committee/')),
                ('about', models.TextField()),
                ('qualification', models.CharField(choices=[('PhD', 'PhD.'), ('Masters', 'Masters'), ('Bachelors', 'Bachelors Degree/HND'), ('NCE', 'NCE'), ('Diploma', 'Diploma'), ('SSCE', 'SSCE')], max_length=200)),
                ('experience', models.PositiveIntegerField(default=1)),
                ('active', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Foundation Committee',
                'verbose_name_plural': 'Foundation Committee',
            },
        ),
    ]
