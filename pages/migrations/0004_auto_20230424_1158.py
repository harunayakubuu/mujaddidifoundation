# Generated by Django 3.2.16 on 2023-04-24 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20230424_1143'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='even_date',
            new_name='event_date',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='even_end_time',
            new_name='event_end_time',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='even_venue',
            new_name='event_location',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='even_picture',
            new_name='event_picture',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='even_start_time',
            new_name='event_start_time',
        ),
        migrations.AlterField(
            model_name='foundationcommittee',
            name='designation',
            field=models.CharField(choices=[('CHAIRMAN', 'Chairman'), ('Secretary', 'Secretary'), ('Auditor', 'Auditor'), ('CHAIRMAN', 'Chairman'), ('CHAIRMAN', 'Chairman'), ('CHAIRMAN', 'Chairman'), ('CHAIRMAN', 'Chairman'), ('CHAIRMAN', 'Chairman'), ('CHAIRMAN', 'Chairman')], max_length=20),
        ),
    ]
