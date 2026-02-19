from django.urls import path
from .views import recipe_list, recipe_one, recipe_two, RecipeListView, RecipeDetailView
app_name = 'ledger'
urlpatterns=[
    #path('recipes/list', recipe_list,name="recipe-list"),
    path('recipes/list/', RecipeListView.as_view(), name="recipe_list"),
    path('recipe/<int:pk>/', RecipeDetailView.as_view(), name="recipe_detail"),
    # path('recipe/1', recipe_one,name="recipe-one"),
    # path('recipe/2', recipe_two,name="recipe-two"),
    # fix the paths
]