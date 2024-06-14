from django.shortcuts import render
from . import models


def all_products(request):
    if request.method == "GET":
        products = models.Product.objects.filter().order_by("-id")
        return render(
            request,
            template_name="products/all_products.html",
            context={"products": products},
        )


def eat_food(request):
    if request.method == "GET":
        eat_food = models.Product.objects.filter(tags__name="покушать").order_by("-id")
        return render(
            request,
            template_name="products/eat_food.html",
            context={"eat_food": eat_food},
        )


def drinks(request):
    if request.method == "GET":
        drinks = models.Product.objects.filter(tags__name="попить").order_by("-id")
        return render(
            request, template_name="products/drinks.html", context={"drinks": drinks}
        )
