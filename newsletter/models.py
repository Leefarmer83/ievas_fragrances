from django.db import models

# Create your models here.


class Subscriber(models.Model):
    """
    A subscriber model for capturing subscribers for the newsletter
    """

    email = models.EmailField(max_length=255, unique=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
