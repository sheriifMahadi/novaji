from django.db import models

class Register(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=11)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=200)
    DOB = models.DateTimeField()

    def __str__(self):
        return f"{self.firstName} {self.last_name}"
        