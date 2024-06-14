from django import forms
from . import models


class PhoneForm(forms.ModelForm):
    class Meta:
        model = models.Phone
        fields = "__all__"
