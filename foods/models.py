from django.db import models


class Food(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True)
    calories = models.FloatField(default=0.0)
    price = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title


WEEK_CHOICES = (
    ("Monday", "Monday"),
    ("Tuesday", "Tuesday"),
    ("Wednesday","Wednesday"),
    ("Thursday", "Thursday"),
    ("Friday", "Friday"),
    ("Saturday", "Saturday"),
    ("Sunday", "Sunday"),
)


CATEGORY_CHOICES = (
    ("Sets", "Sets"),
    ("Lunch", "Lunch"),
    ("BreakFast", "BreakFast"),
    ("Dinner", "Dinner"),
)


class Weeks(models.Model):
    food = models.ManyToManyField(Food)
    week = models.CharField(choices=WEEK_CHOICES, max_length=25, default=WEEK_CHOICES[0][0])
    def __str__(self):
        return f"For {self.week} recommended {self.food.all()}"

class Category(models.Model):
    category = models.ManyToManyField(Food)
    category_type = models.CharField(choices=CATEGORY_CHOICES, max_length=25)
    def __str__(self):
        return f"{self.category_type} : {self.category.all()}"
# Create your models here.
