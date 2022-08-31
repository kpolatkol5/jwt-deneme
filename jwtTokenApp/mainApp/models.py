from msilib.schema import Class
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User


class Person(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="profil")
    menu = models.CharField(null=True,blank=True,max_length=50 , verbose_name="Menu alanı" , choices={("orders","orders"),("sales","sales"),("customers","customers"),("calender","calender"),("products","products")})
    show = models.BooleanField(default=False,verbose_name="Gösterilsin mi")
    position = models.CharField(null=True,blank=True,choices={("top_right","top_right"),("bottom_left","bottom_left"),("top_left","top_left")} , max_length=50)

    def __str__(self):
        return str(self.user)