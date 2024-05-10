from django.urls import path
from . import views

urlpatterns = [
    path('products_all/', views.all_products, name='all_products'),
    path('eat_food/', views.eat_food, name='eat_food'),
    path('drinks/', views.drinks, name='drinks'),
]
