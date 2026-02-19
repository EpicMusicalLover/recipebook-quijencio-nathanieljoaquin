from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Recipe

def recipe_list(request):
    recipes = Recipe.objects.all()
    ctx = {"recipes":recipes}
    return render(request, 'recipe_list.html',ctx)

class RecipeListView(ListView):
    model = Recipe
    template_name = "recipe_list.html"

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "recipe_list.html"

# def recipe_list(request):
#     ctx={
#         "recipes": [
#             {
#                 "name": "Recipe 1",
#                 "ingredients": [
#                     {
#                         "name": "tomato",
#                         "quantity": "3pcs"
#                     },
#                     {
#                         "name": "onion",
#                         "quantity": "1pc"
#                     },
#                     {
#                         "name": "pork",
#                         "quantity": "1kg"
#                     },
#                     {
#                         "name": "water",
#                         "quantity": "1L"
#                     },
#                     {
#                         "name": "sinigang mix",
#                         "quantity": "1 packet"
#                     }
#                 ],
#                 "link": "/recipe/1"
#             },
#             {
#                 "name": "Recipe 2",
#                 "ingredients": [
#                     {
#                         "name": "garlic",
#                         "quantity": "1 head"
#                     },
#                     {
#                         "name": "onion",
#                         "quantity": "1pc"
#                     },
#                     {
#                         "name": "vinegar",
#                         "quantity": "1/2cup"
#                     },
#                     {
#                         "name": "water",
#                         "quanity": "1 cup"
#                     },
#                     {
#                         "name": "salt",
#                         "quantity": "1 tablespoon"
#                     },
#                     {
#                         "name": "whole black peppers",
#                         "quantity": "1 tablespoon"
#                     },
#                     {
#                         "name": "pork",
#                         "quantity": "1 kilo"
#                     }
#                 ],
#                 "link": "/recipe/2"
#             }
#         ]
#     }
#     return render(request, 'recipe_list.html',ctx)

def recipe_one(request):
    recipe = {
        "name": "Recipe 1",
        "ingredients": [
            {
                "name": "tomato",
                "quantity": "3pcs"
            },
            {
                "name": "onion",
                "quantity": "1pc"
            },
            {
                "name": "pork",
                "quantity": "1kg"
            },
            {
                "name": "water",
                "quantity": "1L"
            },
            {
                "name": "sinigang mix",
                "quantity": "1 packet"
            }
        ],
    }
    ctx={"recipe":recipe}
    return render(request, 'recipe_details.html', ctx)

def recipe_two(request):
    recipe = {
        "name": "Recipe 2",
        "ingredients": [
            {
                "name": "garlic",
                "quantity": "1 head"
            },
            {
                "name": "onion",
                "quantity": "1pc"
            },
            {
                "name": "vinegar",
                "quantity": "1/2cup"
            },
            {
                "name": "water",
                "quantity": "1 cup"
            },
            {
                "name": "salt",
                "quantity": "1 tablespoon"
            },
            {
                "name": "whole black peppers",
                "quantity": "1 tablespoon"
            },
            {
                "name": "pork",
                "quantity": "1 kilo"
            }
        ],
    }
    ctx={"recipe":recipe}
    return render(request, 'recipe_details.html', ctx)

# Create your views here.
