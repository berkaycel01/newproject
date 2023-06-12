from django.db import models


class Article(models.Model):
    name = models.CharField(max_length=55)
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to='article/images')


    def __str__(self):
        return self.name