from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [

    path("logout/", views.log_out, name="logout"),
    path('accounts/login/', auth_views.LoginView.as_view(), name="login"),

    path('', views.HomeView.as_view(), name='home'),
    path('revenues/', views.RevenuesView, name="revenues"),

    path('purchases/', views.PurchaseList.as_view(), name = "purchases"),
    path('purchases/new', views.PurchaseCreate.as_view(), name="new_purchase"),

    path('ingredients/', views.IngredientList.as_view(), name="ingredients"),
    path('ingredients/new/', views.IngredientCreate.as_view(), name="new_ingredient"),
    path('ingredients/<pk>/update', views.IngredientUpdate.as_view(), name="update_ingredient"),
    path('ingredients/<pk>/delete', views.IngredientDelete.as_view(), name="delete_ingredient"),
    
    path('menus/', views.MenuList.as_view(), name="menus"),
    path('menus/new/', views.MenuCreate.as_view(), name="new_menu"),
    path('menus/<pk>/update', views.MenuUpdate.as_view(), name="update_menu"),
    path('menus/<pk>/delete', views.MenuDelete.as_view(), name="delete_menu"),

    path('recipes/new/', views.RecipeCreate.as_view(), name="new_recipe"),

]