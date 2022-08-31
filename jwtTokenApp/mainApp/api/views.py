from rest_framework import generics
from rest_framework.permissions import IsAuthenticated ,AllowAny
from mainApp.models import Person
from mainApp.api.serializers import PersonSerializer
# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.generics import CreateAPIView

from mainApp.api.serializers import LoginSerializer

class PersonList(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = (AllowAny,) # jwt token ile login işlemi yapamadığım için izinleri herkese açık yapıyorum
    


class PersonListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = (AllowAny,)

    # detayları görüntülemek için




class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer
    # permission_classes = (IsAuthenticated,)
