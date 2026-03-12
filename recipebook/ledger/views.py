from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
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
    template_name = "recipe_add.html"
    form_class = RecipeForm

class RecipeImageCreateView(LoginRequiredMixin, CreateView):
    model = RecipeImage
    form_class = RecipeImageForm
    template_name = "recipe_add_image.html"
    def get_context_data(self, **kwargs): #to show the dropdown list
        context = super().get_context_data(**kwargs)
        context['taskgroup']=TaskGroup.objects.all()
        context['form']=TaskForm()
        return context
    def post(self, request, *args, **kwargs): #whenever you type, itll post on the website
        form = TaskForm(request.POST)
        if form.is_valid():
    def get_success_url(self):
        return reverse_lazy('url name', kwargs={ 'pk': self.object.pk })


# Create your views here.
