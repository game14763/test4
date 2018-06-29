from django import forms
from food.models import Food

class FoodForm(forms.ModelForm):
    food = forms.CharField(
                    label='Add food to menu',
                    max_length=100,
                    widget=forms.TextInput(attrs={'placeholder':'Enter your own menu'}))
    sugar = forms.CharField(
                    label='Sugar(%)',
                    max_length=3)
    class Meta():
        model = Food
        fields = '__all__'
