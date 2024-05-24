from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models


class CustomUser(User):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    phone_number = models.CharField(max_length=14, default="+996")
    age = models.PositiveIntegerField(default=18, validators=[MinValueValidator(5), MaxValueValidator(99)])
    gender = models.CharField(max_length=100, choices=GENDER)
    club = models.CharField(max_length=100, default="Клуб не определен")


# Для проверки обработки сигнала - есть ли подключение к middleware
@receiver(post_save, sender=CustomUser)
def set_club(sender, instance, created, **kwargs):
    if created:
        print("Сигнал обработан пользователь создан")
        age = instance.age
        if age < 5:
            instance.club = 'Детский'
        elif age >= 5 and age <= 10:
            instance.club = 'Детский'
        elif age >= 11 and age <= 18:
            instance.club = 'Подростковый'
        elif age >= 18 and age <= 45:
            instance.club = 'Взрослый'
        else:
            instance.club = 'Клуб не определен'
        instance.save()
