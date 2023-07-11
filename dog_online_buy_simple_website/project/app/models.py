from django.db import models

# Create your models here.
class Website(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to="media")

    def __str__(self) -> str:
        return self.title