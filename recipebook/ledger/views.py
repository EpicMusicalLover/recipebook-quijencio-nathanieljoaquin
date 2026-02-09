from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('Recipe Book')

def recipe_list(request):
    if request.method =='POST':
        tasks.append(request.POST.get('task_name'))
    ctx={"tasks":tasks}
    return render(request, 'recipe_list.html', ctx)
tasks = ['Recipe 1', 'Recipe 2']

def recipe_one(request):
    recipe = {
        "name": "Recipe 1",
        "ingredients": [
            {"name": "tomato", "quantity": "3pcs"},
            {"name": "onion", "quantity": "1pc"},
            {"name": "pork", "quantity": "1kg"},
            {"name": "water", "quantity": "1L"},
            {"name": "sinigang mix", "quantity": "1 packet"}
        ],
        "link": "/ledger/recipe/1"
    }
    ctx={"recipe":recipe}
    return render(request, 'recipe_one.html', ctx)

def recipe_two(request):
    if request.method =='POST':
        tasks.append(request.POST.get('task_name'))
    ctx={"tasks":tasks}
    return render(request, 'recipe_list.html', ctx)
tasks = ['Recipe 1', 'Recipe 2']

# Create your views here.
