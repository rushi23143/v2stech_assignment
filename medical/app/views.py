from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth
from .forms import LoginForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def login(request):
    if request.user.is_authenticated:
        auth.logout(request)
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('manage_store')
            else:
                messages.error(request, 'Invalid Credentials!', extra_tags='login')
                return redirect('login')
    else:
        login_form = LoginForm()
    return render(request, 'login.html', {'form': login_form})

def manage_store(request):
    if not request.user.is_authenticated:
        return redirect('login')
    store_list = MedicalStore.objects.all()
    return render(request, 'manage_store.html', {'store_list':store_list})

def add_store(request):
    if not request.user.is_authenticated:
        return redirect('login')
    storetype = StoreType.objects.all()
    if request.POST:
        store_name = request.POST['storename']
        username = request.POST['username']
        password = request.POST['password']
        store_email_id = request.POST['email']
        mobile_number = request.POST['mobile']
        address_1 = request.POST['address1']
        address_2 = request.POST['address2']
        store_licence = request.POST.get('storelic')
        if request.POST['storetype']:
            store_type_id = request.POST['storetype']
        else:
            store_type_id = None
        #store_type_id = request.POST['storetype']
        store_type = StoreType.objects.get(id=store_type_id)
        store_registration_no = request.POST['regno']
        
        if MedicalStore.objects.filter(username=username).exists():
            error = 'yes'
            messages.error(request, 'Username Must be Unique!')
            return render(request, 'add_store.html', {
                "error": error, 'storename': store_name, 'username': username, 'password': password,
                'email': store_email_id, 'mobile': mobile_number, 'address1': address_1, 'address2': address_2, 'storelic': store_licence,
                'storetype1': store_type_id, 'regno': store_registration_no, 'storetype':storetype})

        if MedicalStore.objects.filter(store_email_id=store_email_id).exists():
            error = 'yes'
            messages.error(request, 'Store Email-id Must be Unique!')
            return render(request, 'add_store.html', {
                "error": error, 'storename': store_name, 'username': username, 'password': password,
                'email': store_email_id, 'mobile': mobile_number, 'address1': address_1, 'address2': address_2, 'storelic': store_licence,
                'storetype1': store_type_id, 'regno': store_registration_no, 'storetype':storetype})

        else:
            if len(password)>10 or len(password)<6:
                error = 'yes'
                messages.error(request, 'password length should be between 6 to 10 character')
                return render(request, 'add_store.html', {
                "error": error, 'storename': store_name, 'username': username, 'password': password,
                'email': store_email_id, 'mobile': mobile_number, 'address1': address_1, 'address2': address_2, 'storelic': store_licence,
                'storetype1': store_type_id, 'regno': store_registration_no, 'storetype':storetype})
            else:
                error = 'no'
                MedicalStore.objects.create(store_name=store_name, username=username, password=password, store_email_id=store_email_id,
                mobile_number=mobile_number, address_1=address_1, address_2=address_2, store_licence=store_licence,
                store_type=store_type, store_registration_no=store_registration_no)
                #return redirect("manage_store")
            User.objects.create_user(username=username, password=password)
            return redirect('manage_store')

        
    return render(request, 'add_store.html', {'storetype': storetype})

def edit_store(request, id):
    if not request.user.is_authenticated:
        return redirect('login')
    store = MedicalStore.objects.get(id=id)
    storetype = StoreType.objects.all()
    user = User.objects.get(username=store.username)
    if request.POST:
        store_name = request.POST['storename']
        username = request.POST['username']
        password = request.POST['password']
        store_email_id = request.POST['email']
        mobile_number = request.POST['mobile']
        address_1 = request.POST['address1']
        address_2 = request.POST['address2']
        store_licence = request.POST.get('storelic')
        if request.POST['storetype']:
            store_type_id = request.POST['storetype']
        else:
            store_type_id = None
        #store_type_id = request.POST['storetype']
        store_type = StoreType.objects.get(id=store_type_id)
        store_registration_no = request.POST['regno']
        
        if username != store.username and MedicalStore.objects.filter(username=username).exists():
            error = 'yes'
            messages.error(request, 'Username Must be Unique!')
            return render(request, 'edit_store.html', {
                "error": error, 'storename': store_name, 'username': username, 'password': password,
                'email': store_email_id, 'mobile': mobile_number, 'address1': address_1, 'address2': address_2, 'storelic': store_licence,
                'storetype1': store_type_id, 'regno': store_registration_no, 'storetype':storetype})

        if store_email_id != store.store_email_id and MedicalStore.objects.filter(store_email_id=store_email_id).exists():
            error = 'yes'
            messages.error(request, 'Store Email-id Must be Unique!')
            return render(request, 'edit_store.html', {
                "error": error, 'storename': store_name, 'username': username, 'password': password,
                'email': store_email_id, 'mobile': mobile_number, 'address1': address_1, 'address2': address_2, 'storelic': store_licence,
                'storetype1': store_type_id, 'regno': store_registration_no, 'storetype':storetype})

        else:
            if len(password)>10 or len(password)<6:
                error = 'yes'
                messages.error(request, 'password length should be between 6 to 10 character')
                return render(request, 'edit_store.html', {
                "error": error, 'storename': store_name, 'username': username, 'password': password,
                'email': store_email_id, 'mobile': mobile_number, 'address1': address_1, 'address2': address_2, 'storelic': store_licence,
                'storetype1': store_type_id, 'regno': store_registration_no, 'storetype':storetype})
            else:
                error = 'no'
                store.store_name = store_name
                store.username = username
                store.password = password
                store.store_email_id = store_email_id
                store.mobile_number = mobile_number
                store.address_1 = address_1
                store.address_2 = address_2
                store.store_licence = store_licence
                #store.store_type = request.POST['storetype']
                store.store_type_id = store_type
                #store.store_type = StoreType.objects.get(id=store.store_type_id)
                store.store_registration_no = store_registration_no
                store.save()
                user.username = username
                user.set_password(password)
                user.save()
                return redirect("manage_store")
    return render(request, 'edit_store.html', {'store':store, 'storetype':storetype})

def delete_store(request, id):
    if not request.user.is_authenticated:
        return redirect('login')
    username = MedicalStore.objects.get(id=id).username
    user = User.objects.get(username=username)
    user.delete()
    medical = MedicalStore.objects.get(id=id)
    med = MedicineDetails.objects.filter(store=medical).update(store=None)
    medical.delete()
    return redirect("manage_store")

def manage_medicine(request):
    if not request.user.is_authenticated:
        return redirect('login')
    medicine_list = MedicineDetails.objects.all()
    return render(request, 'manage_medicine.html', {'medicine_list':medicine_list})

def add_medicine(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.POST:
        medicine_name = request.POST['medicinename']
        medicine_details = request.POST['medicinedetails']
        medicine_price = request.POST['price']
        medicine_quantity = request.POST['quantity']
        medicine_expiry_date = request.POST['date']
        store_id = request.POST['medicinestore']
        store = MedicalStore.objects.get(id=store_id)
        medicine_type_id = request.POST['medicinetype']
        medicine_type = MedicineType.objects.get(id=medicine_type_id)
        print(medicine_type_id)
        print(store)
        try:
            MedicineDetails.objects.create(medicine_name=medicine_name, medicine_price=medicine_price, medicine_details=medicine_details,
            medicine_quantity=medicine_quantity, medicine_expiry_date=medicine_expiry_date, store=store, medicine_type=medicine_type)
            return redirect("manage_medicine")
        except Exception as e:
            print(e)
    return render(request, 'add_medicine.html', {'medtype':MedicineType.objects.all(), 'storename':MedicalStore.objects.all()})

def delete_medicine(request, id):
    if not request.user.is_authenticated:
        return redirect('login')
    MedicineDetails.objects.get(pk=id).delete()
    return redirect('manage_medicine')

def edit_medicine(request, id):
    if not request.user.is_authenticated:
        return redirect('login')
    medicine = MedicineDetails.objects.get(id=id)
    medtype = MedicineType.objects.all()
    storename = MedicalStore.objects.all()
    if request.POST:
        medicine_name = request.POST['medicinename']
        medicine_details = request.POST['medicinedetails']
        medicine_price = request.POST['price']
        medicine_quantity = request.POST['quantity']
        medicine_expiry_date = request.POST['date']
        store_id = request.POST['medicinestore']
        store = MedicalStore.objects.get(id=store_id)
        medicine_type_id = request.POST['medicinetype']
        medicine_type = MedicineType.objects.get(id=medicine_type_id)

        medicine.medicine_name = medicine_name
        medicine.medicine_details = medicine_details
        medicine.medicine_price = medicine_price
        medicine.medicine_quantity = medicine_quantity
        medicine.medicine_expiry_date = medicine_expiry_date
        medicine.store_id = store_id
        #medicine.store = MedicalStore.objects.get(id=medicine.store_id)
        medicine.medicine_type_id = medicine_type
        #medicine.medicine_type = MedicineType.objects.get(id=medicine.medicine_type_id)
        medicine.store = store
        #medicine.medicine_type = request.POST['medicinetype']
        medicine.save()
        return redirect("manage_medicine")
    return render(request, 'edit_medicine.html', {'medicine':medicine, 'medtype':medtype, 'storename':storename})

def logout(request):
    auth.logout(request)
    return redirect('login')