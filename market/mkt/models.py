from django.db import models
from django.core.validators import MinLengthValidator
from django.conf import settings

# Create your models here.
class Ad(models.Model):
    title = models.CharField(max_length=200, validators=[MinLengthValidator(2, "Title must be at least 2 characters long")])
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    text = models.TextField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
