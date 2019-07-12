from django import forms
from .models import Restaurant

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = '__all__'

class UpdateRestaurantForm(forms.ModelForm):
	class Meta:
		model = Restaurant
		fields = ["description","opening_time","closing_time"]
