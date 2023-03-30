from django.db import models

# Create your models here.
class Ingredient(models.Model):
    GRAMS = 'g'
    TABLESPOON = 'Tbsp'
    MILLILITER = "mL"
    EGGS = "eggs"
    UNIT_CHOICES = [
        (EGGS, "eggs"),
        (GRAMS,'grams'),
        (TABLESPOON, 'tablespoon'),
        (MILLILITER, 'milliliter'),

    ]
    name = models.CharField(max_length=20)
    quantity = models.PositiveIntegerField()
    unit = models.CharField(max_length=4,choices=UNIT_CHOICES)
    price = models.FloatField()

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return "/ingredients"

class MenuItem(models.Model):
    title = models.CharField(max_length=30)
    price = models.FloatField()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return "/menus"

class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.menu_item
    
    def get_absolute_url(self):
        return "/menus"

class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem,on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.menu_item
    def get_absolute_url(self):
        return "/purchases"