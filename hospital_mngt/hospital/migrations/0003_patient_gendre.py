# Generated by Django 4.2.7 on 2023-12-07 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0002_rename_name_patient_name_remove_patient_mobile_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='gendre',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
