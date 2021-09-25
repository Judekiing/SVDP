from django.db import models
from django.urls import reverse
from django.db.models.deletion import CASCADE

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User', on_delete=CASCADE,
    )
    body = models.TextField()
    time = models.TimeField
    location = models.TextField
    date = models.DateField
    created_at = models.DateField

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('annou_detail', args=[self.id])

