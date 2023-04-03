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
    price_per_unit = models.FloatField()

    def __str__(self):
        return f"""
        name={self.name};
        qty={self.quantity};
        unit={self.unit};
        unit_price={self.price_per_unit}
        """

    def get_absolute_url(self):
        return "/ingredients"

class MenuItem(models.Model):
    title = models.CharField(max_length=30)
    price = models.FloatField()

    def available(self):
        return all(X.enough() for X in self.reciperequirement_set.all())
    
    def __str__(self):
        return f"title={self.title}; price={self.price}"
    
    def get_absolute_url(self):
        return "/menus"
    

class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"menu_item=[{self.menu_item.__str__()}]; ingredient={self.ingredient.name}; qty={self.quantity}"
    
    def get_absolute_url(self):
        return "/menus"
    
    def enough(self):
        return self.quantity <= self.ingredient.quantity


class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem,on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"menu_item=[{self.menu_item.__str__()}]; time={self.timestamp}"
    
    def get_absolute_url(self):
        return "/purchases"
