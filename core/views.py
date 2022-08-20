from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Chat


@api_view(["GET", "POST"])
def index(request):
    if request.method == "POST":
        # get POST data
        room_name = request.POST.get("room_name", None)
        user_name = request.POST.get("user_name", None)
        user_message = request.POST.get("user_message", None)

        # handle invalid POST data
        if room_name == None or user_name == None or user_message == None:
            response = {
                "status_code": 400,
                "message": "Invalid POST data.",
                "data": {},
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        # process the request
        chat = Chat(room_name=room_name, user=user_name, message=user_message)
        chat.save()  # save the chat to database

        response = {
            "status_code": 200,
            "message": "Success.",
            "data": {},
        }
        return Response(response, status=status.HTTP_201_CREATED)

    if request.method == "GET":
        room_name = request.GET.get("room_name", None)

        # handle invalid room_name
        if room_name == None:
            response = {
                "status_code": 404,
                "message": "room_name cannot  be empty.",
                "data": {},
            }
            return Response(response, status=status.HTTP_404_NOT_FOUND)

        # get all chat from database
        chats = Chat.objects.filter(room_name=room_name).order_by("-id")

        if chats.exists() == False:
            response = {
                "status_code": 404,
                "message": "Invalid Room Name.",
                "data": {},
            }
            return Response(response, status=status.HTTP_404_NOT_FOUND)

        _chat = []
        for chat in chats:
            _chat.append(
                {
                    "user": chat.user,
                    "message": chat.message,
                    "created_at": chat.created_at.timestamp(),
                }
            )

        response = {
            "status_code": 200,
            "message": "Success.",
            "data": {"room_name": room_name, "chats": _chat},
        }
        return Response(response)

    return Response({})
