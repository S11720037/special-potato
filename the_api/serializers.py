from rest_framework import serializers

from .models import User


class UserSerializer(serializers.Serializer):

    username = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=50)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    telephone = serializers.CharField(max_length=15)
    profile_image = serializers.ImageField(max_length=100)
    address = serializers.CharField(max_length=150)
    city = serializers.CharField(max_length=100)
    province = serializers.CharField(max_length=100)
    country = serializers.CharField(max_length=50)

    # class Meta:
    #     model = User
    #     fields = (
    #         "username",
    #         # "password",
    #         "first_name",
    #         "last_name",
    #         "telephone",
    #         "profile_image",
    #         "address",
    #         "city",
    #         "province",
    #         "country",
    #     )
