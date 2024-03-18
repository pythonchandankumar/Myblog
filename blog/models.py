from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.CharField( max_length=100000)
    author=models.CharField(max_length=100)
    photo=models.ImageField(upload_to='myimg')
    publication_date=models.DateTimeField(auto_now_add=True)
