from django.db import models

# Create your models here.

class Note(models.Model):

    def __str__(self) -> str:
        return self.title

    title = models.CharField(max_length=40)
    pub_date = models.DateTimeField('date created')
    content = models.TextField('content', default='')
    