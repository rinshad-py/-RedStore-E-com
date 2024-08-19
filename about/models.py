from django.db import models

# Create your models here.

class UserProfile(models.Model):
    cv = models.FileField(upload_to='cv/')
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "User Profile"

        