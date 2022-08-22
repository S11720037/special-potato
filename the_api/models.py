from django.db import models
from django.contrib.auth.models import User


class User(models.Model):
    django_user = models.ForeignKey(User, on_delete=models.CASCADE)

    username = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    telephone = models.CharField(max_length=15)
    profile_image = models.ImageField(upload_to="profil-picture")
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    country = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
