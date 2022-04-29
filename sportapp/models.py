from django.db import models

# Create your models here.

class Sport(models.Model):
    image = models.CharField(max_length=2000)
    title = models.CharField(max_length=200)
    describe = models.TextField(null=True)
    def __str__(self):
        return self.title

class Comment(models.Model):
    Name = models.CharField(max_length=200)
    Surname = models.CharField(max_length=200)
    Sport = models.CharField(max_length=200, default='football')
    Comment = models.TextField(null=True)
    def __str__(self):
        return self.Name

class Champions(models.Model):
    Name = models.CharField(max_length=100)
    Surname = models.CharField(max_length=100)
    image = models.CharField(max_length=2000)
    description = models.TextField(null=True)
    def __str__(self):
        return self.Name


class Registration(models.Model):
    male = 'M'
    female = 'F'
    male_or_female = [
        (male, 'Male'),
        (female, 'Female')
    ]
    Name = models.CharField(max_length=30)
    Surname = models.CharField(max_length=50)
    Date_of_birth = models.DateField(null=True)
    Male_female = models.CharField(
        max_length = 1,
        choices = male_or_female,
    )
    email = models.EmailField()
    login = models.EmailField(null=True)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.Name