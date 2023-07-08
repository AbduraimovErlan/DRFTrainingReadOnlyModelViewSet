from django.db import models



class Book4(models.Model):
    title = models.CharField(max_length=190)
    descriptions = models.TextField()


    def __str__(self):
        return self.title