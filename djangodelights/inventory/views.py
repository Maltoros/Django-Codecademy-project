from django.shortcuts import render
from .models import Ingredient, MenuItem, RecipeRequirement, Purchase
from .forms import IngredientForm, MenuItemForm, RecipeRequirementForm, PurchaseForm
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.shortcuts import redirect
# Create your views here.



class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "inventory/home.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["ingredients"] = Ingredient.objects.all()
        context["menu_items"] = MenuItem.objects.all()
        context["purchases"] = Purchase.objects.all()
        return context

def RevenuesView(request):
    template_name = "inventory/revenues.html"
    purchases = Purchase.objects.all()
    ingredients = Ingredient.objects.all()
    revenue = 0
    for purchase in purchases:
        revenue += purchase.menu_item.price
    for ingredient in ingredients:
        revenue -= ingredient.price_per_unit * ingredient.quantity

    context = {'revenue' : revenue}

    return render(request, template_name, context)
    




#Ingredient CRUD
class IngredientList(LoginRequiredMixin, ListView):
    template_name = "inventory/ingredients.html"
    model = Ingredient
    ordering = ['name']

class IngredientCreate(LoginRequiredMixin, CreateView):
    template_name = "inventory/new_ingredient.html"
    model = Ingredient
    form_class = IngredientForm

class IngredientUpdate(LoginRequiredMixin, UpdateView):
    template_name = "inventory/update_ingredient.html"
    model = Ingredient
    form_class = IngredientForm

class IngredientDelete(LoginRequiredMixin, DeleteView):
    template_name = "inventory/delete_ingredient.html"
    model = Ingredient
    success_url = "ingredients.html"

#Menu CRUD
class MenuList(LoginRequiredMixin, ListView):
    template_name = "inventory/menu_items.html"
    model = MenuItem
    ordering = ['title']

class MenuCreate(LoginRequiredMixin, CreateView):
    template_name = "inventory/new_menu.html"
    model = MenuItem
    form_class = MenuItemForm

class MenuUpdate(LoginRequiredMixin, UpdateView):
    template_name = "inventory/update_menu.html"
    model = MenuItem
    form_class = MenuItemForm

class MenuDelete(LoginRequiredMixin, DeleteView):
    template_name = "inventory/delete_menu.html"
    model = MenuItem
    success_url = "menu_items.html"

#Recipe requirement
class RecipeCreate(LoginRequiredMixin, CreateView):
    template_name = "inventory/new_recipe.html"
    model = RecipeRequirement
    form_class = RecipeRequirementForm

#Purchase C-R
class PurchaseList(LoginRequiredMixin, ListView):
    template_name = "inventory/purchases.html"
    model = Purchase
    ordering = ['timestamp']

class PurchaseCreate(LoginRequiredMixin, CreateView):
    template_name = "inventory/new_purchase.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["menu_items"] = [X for X in MenuItem.objects.all() if X.available()]
        return context

    def post(self, request):
        menu_item_id = request.POST["menu_item"]
        menu_item = MenuItem.objects.get(pk=menu_item_id)
        requirements = menu_item.reciperequirement_set
        purchase = Purchase(menu_item=menu_item)

        for requirement in requirements.all():
            required_ingredient = requirement.ingredient
            required_ingredient.quantity -= requirement.quantity
            required_ingredient.save()

        purchase.save()
        return redirect("/purchases")

def log_out(request):
    logout(request)
    return redirect("/")



    
    
    
    


