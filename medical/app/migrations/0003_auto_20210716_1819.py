# Generated by Django 3.1.5 on 2021-07-16 12:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210715_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicinedetails',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.medicalstore'),
        ),
    ]
