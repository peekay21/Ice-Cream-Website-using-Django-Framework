from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=255) #name columns
    email =models.CharField(max_length=255) # Email
    phone = models.CharField(max_length=255) # Phone
    msg = models.TextField() # Message
    date = models.DateField()

    def __str__(self):
        return self.name
