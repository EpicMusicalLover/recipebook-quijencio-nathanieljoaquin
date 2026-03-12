from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Recipe, RecipeImage
from .forms import RecipeForm, RecipeImageForm


class RecipeListView(ListView):
    model = Recipe
    template_name = "recipe_list.html"


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = "recipe_details.html"

class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    template_name = "recipe_create.html"
    form_class = RecipeForm

class RecipeImageCreateView(LoginRequiredMixin, CreateView):
    model = RecipeImage
    form_class = RecipeImageForm
    template_name = "recipe_add_image.html"
    def form_valid(self, form):
        recipe_pk = self.kwargs['pk']
        form.instance.recipe = Recipe.objects.get(pk=recipe_pk)
        return super().form_valid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recipe_pk = self.kwargs['pk']
        context['recipe'] = Recipe.objects.get(pk=recipe_pk)
        return context
    def get_success_url(self):
        return reverse_lazy('ledger:recipe_detail', kwargs={ 'pk': self.object.pk })


# Create your views here.
