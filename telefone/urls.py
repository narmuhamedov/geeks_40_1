from django.urls import path
from . import views

urlpatterns = [
    path('phone_list/', views.phone_list, name='phone_list'),
    path('phone_list/<int:id>/', views.phone_detail, name='phone_detail'),
]