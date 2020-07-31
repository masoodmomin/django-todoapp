from django.db import models

# Create your models here.
class ToDo(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=200)
    is_completed = models.BooleanField(default=False)
