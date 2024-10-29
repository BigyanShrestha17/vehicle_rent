from django import forms

class BookingForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
    pickup_address = forms.CharField(label='Pickup Address', widget=forms.Textarea)
    people = forms.IntegerField(label='Number of People')
    car_name = forms.CharField(label='Car Name', max_length=100)