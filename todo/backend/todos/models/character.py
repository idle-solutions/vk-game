from django.db import models


class Character(models.Model):

    name = models.CharField(max_length=15, unique=True, primary_key=True)
    experience = models.PositiveIntegerField(default=0)

    @property
    def level(self):
        return self.experience // 100

    @property
    def bp(self):
        return self.level * 100
