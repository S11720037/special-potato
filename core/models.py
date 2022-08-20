from django.db import models


class Chat(models.Model):
    room_name = models.CharField(max_length=50)
    user = models.CharField(max_length=50)
    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.room_name
