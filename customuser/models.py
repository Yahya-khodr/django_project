from django.db import models

# Create your models here.


class customUser(models.Model):

    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)

    def __str__(self) :
        return "{} {}" . format(self.firstName,self.lastName)