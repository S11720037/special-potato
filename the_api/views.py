from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User as DjangoUser

from .serializers import UserSerializer
from .models import User as CustomUser


def index(request):
    return HttpResponse("arter")


@api_view(["POST"])
def register(request):

    if request.method == "POST":
        serializers = UserSerializer(data=request.data)

        if serializers.is_valid() == False:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

        # create django user
        try:
            django_user = DjangoUser.objects.create_user(
                username=serializers.validated_data["username"],
                password=serializers.validated_data["password"],
            )
        except Exception as e:
            return Response(
                {"status_code": 400, "message": str(e), "data": {}},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # save the user to database
        custom_user = CustomUser(
            django_user=django_user,
            username=serializers.validated_data["username"],
            first_name=serializers.validated_data["first_name"],
            last_name=serializers.validated_data["last_name"],
            telephone=serializers.validated_data["telephone"],
            profile_image=serializers.validated_data["profile_image"],
            address=serializers.validated_data["address"],
            city=serializers.validated_data["city"],
            province=serializers.validated_data["province"],
            country=serializers.validated_data["country"],
        )
        custom_user.save()

        response = {"status_code": 201, "message": "User created.", "data": {}}
        return Response(response, status=status.HTTP_201_CREATED)
