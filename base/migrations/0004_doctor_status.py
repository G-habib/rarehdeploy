# Generated by Django 5.0.2 on 2024-05-29 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_patient_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending', max_length=10),
        ),
    ]