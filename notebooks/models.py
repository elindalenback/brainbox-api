from django.db import models
from django.contrib.auth.models import User

# Notebook Model
class Notebook(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    folder_image = models.ImageField(
        upload_to='images/', default='../default_notebook_c2xfrs'
    )
    
    def __str__(self):
        return self.name
