from django.urls import path
from .views import recipe_list, recipe_one, recipe_two
app_name = 'ledger'
urlpatterns=[
    path('recipes/list', recipe_list,name="recipe-list"),
    path('<int:pk>', recipe_list, name="task_detail"),
    path('recipe/1', recipe_one,name="recipe-one"),
    path('recipe/2', recipe_two,name="recipe-two"),
]