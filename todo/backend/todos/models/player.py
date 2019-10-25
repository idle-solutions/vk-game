from django.db import models
from .character import Character


class Player(models.Model):

    vk_id = models.CharField(max_length=24)
    character = models.OneToOneField(Character, on_delete=models.CASCADE)
