from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer
from djoser.serializers import TokenCreateSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils.timezone import now

from rest_framework.response import Response

User = get_user_model()


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id','email','first_name','last_name','password')



# *** Custom Token Create Serializer is now on hold due to not sending access & refresh token ***

# class CustomTokenCreateSerializer(TokenCreateSerializer):
#     def validate(self, attrs):
#         data = super().validate(attrs)
        
#         # Update last_login
#         self.user.last_login = now()
#         self.user.save(update_fields=['last_login'])
        
#         # Generate token
#         refresh = RefreshToken.for_user(self.user)
        
#         data['refresh'] = str(refresh)
#         data['access'] = str(refresh.access_token)
        
#         print(data['refresh'])
#         print(data['access'])
        
#         return data














