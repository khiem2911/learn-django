from django.db import models

# Create your models here.
class Topic(models.Model):
    top_name = models.CharField(max_length=264,unique=True)

    def __str__(self):
        return self.top_name
class Webpage(models.Model):
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    name = models.CharField(max_length=264)
    url = models.URLField(max_length=255)

    def __str__(self):
        return self.name
class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage,on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return self.date.__str__()
class User(models.Model):
    First_Name = models.CharField(max_length=264)
    Last_Name = models.CharField(max_length=264)
    Email = models.EmailField(max_length=264,unique=True)

    def __str__(self) -> str:
        return self.Email
class FormUser(models.Model):
    name = models.CharField(max_length=264)
    email = models.EmailField(max_length=264,unique=True)
    text = models.CharField(max_length=264)

    def __str__(self) -> str:
        return self.email