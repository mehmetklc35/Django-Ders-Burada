from django.db import models

class Banner(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    # img = models.ImageField(upload_to='banner/')

    def __str__(self) -> str:
        return self.title
    

class Result(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    numbers = models.TextField()

    def __str__(self) -> str:
        return self.title


class Team(models.Model):
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    img = models.ImageField(upload_to='banner/')
    


class Service(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self) -> str:
        return self.title
    

class Blog(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self) -> str:
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    email = models.EmailField()
    body = models.TextField()



