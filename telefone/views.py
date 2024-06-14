from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from . import models, forms


# Список телефонов
class PhoneListView(generic.ListView):
    template_name = "phones/phone_list.html"
    context_object_name = "phones"
    model = models.Phone

    def get_queryset(self):
        return self.model.objects.filter().order_by("-id")


# Детальная информация о телефонах
class PhoneDetailView(generic.DetailView):
    template_name = "phones/phone_detail.html"
    context_object_name = "phone_id"

    def get_object(self, **kwargs):
        phone_id = self.kwargs.get("id")
        return get_object_or_404(models.Phone, id=phone_id)


# CREATE
class CreatePhoneView(generic.CreateView):
    template_name = "phones/create_phone.html"
    form_class = forms.PhoneForm
    success_url = "/phone_list/"

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreatePhoneView, self).form_valid(form=form)


# DELETE
class DeletePhoneView(generic.DeleteView):
    template_name = "phones/confirm_delete.html"
    success_url = "/phone_list/"

    def get_object(self, **kwargs):
        phone_id = self.kwargs.get("id")
        return get_object_or_404(models.Phone, id=phone_id)


# Update
class EditPhoneView(generic.UpdateView):
    template_name = "phones/edit.html"
    form_class = forms.PhoneForm
    success_url = "/phone_list/"

    def get_object(self, **kwargs):
        phone_id = self.kwargs.get("id")
        return get_object_or_404(models.Phone, id=phone_id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(EditPhoneView, self).form_valid(form=form)


# Search   f


class SearchPhoneView(generic.ListView):
    template_name = "phones/phone_list.html"
    context_object_name = "phones"
    paginate_by = 5

    def get_queryset(self):
        return models.Phone.objects.filter(title__icontains=self.request.GET.get("q"))

    def get_context_data(self, *, object_list=None, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex["q"] = self.request.GET.get("q")
        return contex
