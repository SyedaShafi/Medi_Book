from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
import re 

def validate_medicine_data(data):
    errors = {}
    if not data.get('name'):
        errors['name'] = "Medicine name is required."

    if not data.get('generic_name'):
        errors['generic_name'] = "Generic name is required."

    if not data.get('manufacturer'):
        errors['manufacturer'] = "Manufacturer is required."

    if not data.get('description'):
        errors['description'] = "Description is required."

    try:
        price = float(data.get('price', 0))
        if price <= 0:
            errors['price'] = "Price must be greater than zero."
    except ValueError:
        errors['price'] = "Price must be a valid number."

    if not data.get('batch_number'):
        errors['batch_number'] = "Batch number is required."

    try:
        stock_quantity = int(data.get('stock_quantity', 0))
        if stock_quantity < 0:
            errors['stock_quantity'] = "Stock quantity cannot be negative."
    except ValueError:
        errors['stock_quantity'] = "Stock quantity must be a valid integer."

    return errors


def HomeView(request):
    query = request.GET.get('search', '').strip()
    if query:
        query_words = [word for word in query.split() if len(word) > 0]
        if query_words:
            q_objects = Q()
            for word in query_words:
                q_objects |= Q(name__icontains=word) | Q(generic_name__icontains=word)
            medicines = MedicineModel.objects.filter(q_objects).distinct()
            
            for medicine in medicines:
                for word in query_words:
                    pattern = re.compile(re.escape(word), re.IGNORECASE)
                    medicine.generic_name = pattern.sub(f'<mark>{word}</mark>', medicine.generic_name)
                    medicine.name = pattern.sub(f'<mark>{word}</mark>', medicine.name)

        else:
            medicines = MedicineModel.objects.all().order_by('-id')
    else:
        medicines = MedicineModel.objects.all().order_by('-id')
    context = {'data': medicines, 'query': query}
    return render(request, 'index.html', context)


def MedicineDescription(request, slug):
    obj = MedicineModel.objects.filter(slug__iexact=slug)
    if obj.exists():
        obj = obj.first()
    else:
        messages.error(request, 'No data Available!')
    return render(request, 'medicine_details.html', context={'data': obj})


@login_required(login_url="login-view")
def AddMedicine(request):
    if request.method == 'POST':
        data = request.POST
        errors = validate_medicine_data(data)
        if errors:
            context = {'errors': errors}
            print(errors)
            return render(request, 'add_medicine.html', context)
        
        name = data.get('name')
        generic_name = data.get('generic_name')
        manufacturer = data.get('manufacturer')
        description = data.get('description')
        price = data.get('price')
        batch_number = data.get('batch_number')
        form = data.get('form')
        stock_quantity = data.get('stock_quantity')

        MedicineModel.objects.create(
            name = name,
            generic_name = generic_name,
            manufacturer = manufacturer,
            description = description,
            price = price,
            batch_number = batch_number,
            form = form,
            stock_quantity = stock_quantity
        )
        messages.success(request, 'Data added successfully!')
        return redirect('home-view')
    return render(request, 'add_medicine.html')


@login_required(login_url="login-view")
def edit_medicien(request, slug):
    try:
        obj = MedicineModel.objects.get(slug=slug)
        if request.method == 'POST':
            data = request.POST
            errors = validate_medicine_data(data)
            if errors:
                context = {'errors': errors, 'data': obj}
                print(errors)
                return render(request, 'add_medicine.html', context)

            obj.name = data.get('name')
            obj.generic_name = data.get('generic_name')
            obj.manufacturer = data.get('manufacturer')
            obj.description = data.get('description')
            obj.price = data.get('price')
            obj.batch_number = data.get('batch_number')
            obj.form = data.get('form')
            obj.stock_quantity = data.get('stock_quantity')
            obj.save()
            messages.success(request, 'Update Successful!')
            return redirect('home-view')
        
        context={'data': obj}
        return render(request, 'add_medicine.html', context=context)
    
    except MedicineModel.DoesNotExist:
        messages.error('Some error occured!')
        return redirect('home-view', context=context)


@login_required(login_url="login-view")
def delete_medicien(request, slug):
    try:  
        obj = MedicineModel.objects.get(slug=slug)
        obj.delete()
        messages.success(request, 'Data Deleted!')
    except MedicineModel.DoesNotExist:
        messages.warning(request, 'Some error, occured!')
    return redirect('home-view')




