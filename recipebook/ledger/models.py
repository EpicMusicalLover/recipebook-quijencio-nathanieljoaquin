from django.db import models
from django.urls import reverse

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('ingredient_detail', args=[str(self.id)])

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('recipe_detail', args=[str(self.id)])

class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=100)
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        related_name='recipe_ingredients'
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='recipe_ingredients'
    )
    def __str__(self):
        return f"{self.quantity} of {self.ingredient.name} in {self.recipe.name}"

class TaskGroup(models.Model):
    name = models.CharField(max_length=50)

class Task(models.Model):
    name = models.CharField(max_length=100)
    due_date = models.DateTimeField(null=False)
    taskgroup = models.ForeignKey(
        TaskGroup, 
        on_delete=models.CASCADE, #if the group is erased, the task is also erased
        related_name='tasks' #refer to all the tasks using related name in the future for easier search
    )

    def __str__(self):
        return f"{self.name} due on {self.due_date}"
    
    def get_absolute_url(self): #will return the url
        return reverse('tasks:task_detail',args=[str(self.id)])
    
    class Meta:
        unique_together = ['due_date','name'] #dont create a duplicate task, another task with same due date and name
        verbose_name = 'task'
        verbose_name_plural = 'tasks'