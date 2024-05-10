from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Phone(models.Model):
    title = models.CharField(max_length=100)
    price = models.PositiveIntegerField(default=1000)

    def __str__(self):
        return self.title


class Review(models.Model):
    review_phone = models.ForeignKey(Phone, on_delete=models.CASCADE,
                                     related_name='review_phone')
    stars = models.PositiveIntegerField(default=5, validators=[MinValueValidator(1), MaxValueValidator(5)])
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.review_phone}-{self.stars}'