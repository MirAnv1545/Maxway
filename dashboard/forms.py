from django import forms
from food.models import *
from . import services
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields= "__all__"
        widgets = {
        "title":forms.TextInput(attrs={'class':'form-control'})
        }

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields= "__all__"
        widgets = {
        "title":forms.TextInput(attrs={'class':'form-control'})
        }

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields= "__all__"
        widgets = {
        "first_name":forms.TextInput(attrs={'class':'form-control'})
        }

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields= "__all__"
        widgets = {
        "customer":forms.TextInput(attrs={'class':'form-control'}),
        "address":forms.TextInput(attrs={'class':'form-control'}),
        "payment_type":forms.NumberInput(attrs={'class':'form-control'}),
        "created_at":forms.Select(attrs={'class':'form-control'}),
        }
