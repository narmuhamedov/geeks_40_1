from django.shortcuts import render, get_object_or_404
from . import models


def phone_list(request):
    if request.method == 'GET':
        phones = models.Phone.objects.filter().order_by('-id')
        return render(request, template_name='phones/phone_list.html',
                      context={'phones': phones})


def phone_detail(request, id):
    if request.method == 'GET':
        phone_id = get_object_or_404(models.Phone, id=id)
        return render(request, template_name='phones/phone_detail.html',
                      context={'phone_id': phone_id})
