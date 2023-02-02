from django.db import models

# Create your models here.

class Post(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/')

    def __str__(self) -> str:
        return f'{self.name} ~ создано ~ {self.created_at} {self.image}'