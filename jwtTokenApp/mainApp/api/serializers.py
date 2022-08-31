import email
from rest_framework import serializers
from mainApp.models import Person

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer



class PersonSerializer(serializers.ModelSerializer):
    # user = serializers.StringRelatedField(read_only=True)

    class Meta:
        
        model = Person
        fields = "__all__"
 





class LoginSerializer(TokenObtainPairSerializer):
    # email = serializers.StringRelatedField(read_only=True)



    @classmethod
    def get_token(cls,user):
        token = super().get_token(user)
        print(token)
        token['username'] = user.username
        token['password'] = user.password

        return token


    def validate(self,attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        data['username'] = self.user.username

        return data



    # def validate(self, attrs):
    #     data = super().validate(attrs)

    #     refresh = self.get_token(self.user)

    #     data["refresh"] = str(refresh)
    #     data["access"] = str(refresh.access_token)

    #     if api_settings.UPDATE_LAST_LOGIN:
    #         update_last_login(None, self.user)

    #     return data