from django.db import models

# Create your models herre
class Todo(models.Model):
    title=models.CharField(max_length=250)

