from django.db import models
from datetime import datetime
from django.template.defaultfilters import slugify

class Categories(models.TextChoices):
    OPTION1 = 'option1'
    OPTION2 = 'option2'
    OPTION3 = 'option3'
    OPTION4 = 'option4'
    OPTION5 = 'option5'
    OPTION6 = 'option6'

class Month(models.TextChoices):
    January = 'JAN'
    February = 'FEB'
    March = 'MAR'
    April = 'APR'
    May = 'MAY'
    June = 'JUN'
    July = 'JUL'
    August = 'AUG'
    September = 'SEP'
    October = 'OCT'
    November = 'NOV'
    December = 'DEC'

class Profession(models.TextChoices):
    Interior_Design = 'Interior Design'
    Architect = 'Architect'
    Modular_Dealer = 'Modular Dealer'

class Blog(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=50 , choices=Categories.choices, default=Categories.OPTION1)
    thumbnail = models.ImageField(upload_to='photos/')
    excerpt = models.CharField(max_length=250)
    month = models.CharField(max_length=3, choices=Month.choices, default=Month.January)
    day = models.CharField(max_length=2)
    content = models.TextField()
    author_name = models.CharField(max_length=50)
    author_title = models.CharField(max_length=50)
    author_image = models.ImageField(upload_to='author/')
    date_created = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title
    

class Contact(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField(max_length=30)
    city = models.CharField(max_length=40)
    message = models.TextField(max_length=500)
    
    def __str__(self):
        return self.name

class Dealer(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField(max_length=30)
    profession = models.CharField(max_length=40, choices=Profession.choices, default=Profession.Interior_Design)
    message = models.TextField(max_length=500)

    def __str__(self):
        return self.name