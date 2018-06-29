from django.shortcuts import render
from food.models import Food
from food.forms import FoodForm

# Create your views here.
def index(request):
    add_food = FoodForm()
    if request.method == 'POST':
        new_food = FoodForm(request.POST)
        if new_food.is_valid():
            new_food.save(commit=True)
        else:
            print("ERROR FORM INVALID")
    return render(request, 'food/index.html', {'add_food':add_food})

def menu(request):
    food_menu = Food.objects.all()
    return render(request, 'food/menu.html', {'food_menu':food_menu})
