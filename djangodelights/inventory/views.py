from django.shortcuts import render
from .models import Ingredient, MenuItem, RecipeRequirement, Purchase
from .forms import IngredientForm, MenuItemForm, RecipeRequirementForm, PurchaseForm
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
# Create your views here.



class HomeView(TemplateView):
    template_name = "inventory/home.html"

class RevenuesView(TemplateView):
    template_name = "inventory/revenues.html"


#Ingredient CRUD
class IngredientList(ListView):
    template_name = "inventory/ingredients.html"
    model = Ingredient
    ordering = ['name']

class IngredientCreate(CreateView):
    template_name = "inventory/new_ingredient.html"
    model = Ingredient
    form_class = IngredientForm

class IngredientUpdate(UpdateView):
    template_name = "inventory/update_ingredient.html"
    model = Ingredient
    form_class = IngredientForm

class IngredientDelete(DeleteView):
    template_name = "inventory/delete_ingredient.html"
    model = Ingredient
    success_url = "ingredients.html"

#Menu CRUD
class MenuList(ListView):
    template_name = "inventory/menu_items.html"
    model = MenuItem
    ordering = ['title']

class MenuCreate(CreateView):
    template_name = "inventory/new_menu.html"
    model = MenuItem
    form_class = MenuItemForm

class MenuUpdate(UpdateView):
    template_name = "inventory/update_menu.html"
    model = MenuItem
    form_class = MenuItemForm

class MenuDelete(DeleteView):
    template_name = "inventory/delete_menu.html"
    model = MenuItem
    success_url = "menu_items.html"

#Recipe requirement
class RecipeCreate(CreateView):
    template_name = "inventory/new_recipe.html"
    model = RecipeRequirement
    form_class = RecipeRequirementForm

#Purchase C-R
class PurchaseList(ListView):
    template_name = "inventory/purchases.html"
    model = Purchase
    ordering = ['timestamp']

class PurchaseCreate(CreateView):
    template_name = "inventory/new_purchase.html"
    model = Purchase
    form_class = PurchaseForm


