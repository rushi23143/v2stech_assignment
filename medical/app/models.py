from django.db import models

# Create your models here.
class StoreType(models.Model):
    id = models.AutoField(primary_key=True) 
    type_name = models.CharField(max_length=45)

    def __str__(self):
        return self.type_name

class MedicalStore(models.Model):
    Licence_Choices = (
        ('0', 'Retail Drug License'),
        ('1', 'Wholesale Drug License'),
    )
    id = models.AutoField(primary_key=True)
    store_name = models.CharField(max_length=50)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=50)
    store_email_id = models.EmailField(max_length=30)
    mobile_number = models.CharField(max_length=10)
    address_1 = models.CharField(max_length=100)
    address_2 = models.CharField(max_length=100)
    store_licence = models.IntegerField(choices=Licence_Choices)
    store_type = models.ForeignKey('StoreType', null=True, on_delete=models.SET_NULL)
    store_registration_no = models.CharField(max_length=100)

    def __str__(self):
        return self.store_name

class MedicineType(models.Model):
    id = models.AutoField(primary_key=True)
    medicine_type_name = models.CharField(max_length=60)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.medicine_type_name

class MedicineDetails(models.Model):
    id = models.AutoField(primary_key=True)
    medicine_name = models.CharField(max_length=60)
    medicine_details = models.CharField(max_length=100)
    medicine_price = models.CharField(max_length=60)
    medicine_quantity = models.CharField(max_length=60)
    medicine_expiry_date = models.DateTimeField()
    store = models.ForeignKey('MedicalStore', null=True, on_delete=models.SET_NULL)
    medicine_type = models.ForeignKey('MedicineType', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.medicine_name