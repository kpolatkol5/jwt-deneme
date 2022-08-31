from django.urls import path
from mainApp.api.views import PersonList ,PersonListDetail

urlpatterns = [
    path("users", PersonList.as_view(), name="kullanicilar"),
    path("users/<int:pk>", PersonListDetail.as_view(), name="kullanici_bilgileri"),

]