from django.urls import path
from . import views

urlpatterns = [
    path("phone_list/", views.PhoneListView.as_view(), name="phone_list"),
    path("phone_list/<int:id>/", views.PhoneDetailView.as_view(), name="phone_detail"),
    path(
        "phone_list/<int:id>/delete/",
        views.DeletePhoneView.as_view(),
        name="delete_phone",
    ),
    path(
        "phone_list/<int:id>/update/",
        views.EditPhoneView.as_view(),
        name="update_phone",
    ),
    path("create_phone/", views.CreatePhoneView.as_view(), name="create_phone"),
    path("search/", views.SearchPhoneView.as_view(), name="search"),
]
