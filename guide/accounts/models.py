from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False)

    REQUIRED_FIELDS = ['date_of_birth']

    def save(self, *args, **kwargs):
        super(CustomUser, self).save(*args, **kwargs)


    def __str__(self):
        return self.first_name + " " + self.last_name