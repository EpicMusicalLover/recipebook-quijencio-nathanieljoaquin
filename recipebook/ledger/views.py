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
    template_name = "recipe_details.html"




# Create your views here.
