from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Person(models.Model):
    name = models.CharField(max_length=100)
    japanese = models.IntegerField('国語', validators=[MinValueValidator(0), MaxValueValidator(100)])
    math = models.IntegerField('算数', validators=[MinValueValidator(0), MaxValueValidator(100)])
    science = models.IntegerField('理科', validators=[MinValueValidator(0), MaxValueValidator(100)])
    social = models.IntegerField('社会', validators=[MinValueValidator(0), MaxValueValidator(100)])
    english = models.IntegerField('英語', validators=[MinValueValidator(0), MaxValueValidator(100)])