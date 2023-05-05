from django.db import models

# Create your models here.


class EmailSend(models.Model):
    email = models.EmailField(max_length=155)
    subject = models.CharField(max_length=495)
    message = models.TextField(max_length=2499)

