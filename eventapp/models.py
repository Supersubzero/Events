from django.db import models
from django.contrib.auth.models import User

class Venue(models.Model):

    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Event(models.Model):
    title = models.CharField(max_length=200)
    discription = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    venue = models.ForeignKey(Venue,on_delete=models.CASCADE)
    organizer = models.ForeignKey(User,on_delete=models.CASCADE)
