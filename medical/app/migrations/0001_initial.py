# Generated by Django 3.1.5 on 2021-07-14 05:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MedicalStore',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('store_name', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=50)),
                ('store_email_id', models.EmailField(max_length=30)),
                ('mobile_number', models.CharField(max_length=10)),
                ('address_1', models.CharField(max_length=100)),
                ('address_2', models.CharField(max_length=100)),
                ('store_licence', models.IntegerField(choices=[('0', 'Retail Drug License'), ('1', 'Wholesale Drug License')])),
                ('store_registration_no', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MedicineType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('medicine_type_name', models.CharField(max_length=60)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='StoreType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type_name', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='MedicineDetails',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('medicine_name', models.CharField(max_length=60)),
                ('medicine_details', models.CharField(max_length=100)),
                ('medicine_price', models.CharField(max_length=60)),
                ('medicine_quantity', models.CharField(max_length=60)),
                ('medicine_expiry_date', models.DateTimeField()),
                ('medicine_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.medicinetype')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.medicalstore')),
            ],
        ),
        migrations.AddField(
            model_name='medicalstore',
            name='store_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.storetype'),
        ),
    ]