from django.shortcuts import render, redirect
from .models import *
from .forms import BookingForm

def home(request):
    return render(request, 'home.html', {})


def about(request):
    return render(request, 'about.html', {})


def services(request):
    return render(request, 'services.html', {})


def gallery(request):
    return render(request, 'gallery.html', {})


def client(request):
    return render(request, 'client.html', {})


def contact(request):
    return render(request, 'contact.html', {})


def search(request):
    if request.method == "POST":
        brand = request.POST.get('brand')
        car_type = request.POST.get('car_type')

        # Filter cars based on the search criteria
        cars = Car.objects.all()
        if brand:
            cars = cars.filter(brand__name=brand)
        if car_type:
            cars = cars.filter(car_type__name=car_type)
        return render(request, 'search.html', {'cars': cars})

    return render(request, 'home.html')




def book_now(request):
    car_name = request.GET.get('car_name', '')
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            # Process the form data
            return redirect('success')
    else:
        form = BookingForm(initial={'car_name': car_name})
    return render(request, 'book_now.html', {'form': form})