# Generated by Django 4.2.7 on 2023-12-07 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0003_patient_gendre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='gendre',
        ),
        migrations.AddField(
            model_name='patient',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=10),
        ),
    ]