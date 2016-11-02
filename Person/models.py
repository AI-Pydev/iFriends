from django.db import models
from django.contrib.auth.models import User


gender_list = (('M', 'Male'), ('F', 'Female' ))

class Blog(models.Model):
    title = models.CharField('Title', max_length=200)
    text = models.TextField('Text', max_length=204)
    date = models.DateTimeField(default='2016-07-06 15:35:09.000000')

    def __str__(self):
        return self.title

class Person(models.Model):
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=1, choices=gender_list, default='N')
    birthday = models.DateTimeField('Birthday')
    email = models.EmailField('Email')
    favouriteURL = models.URLField('myURL', null=True)
    desc = models.TextField('Desc', max_length=500, null=True)
    friends = models.ManyToManyField('self', blank=True)
    blogs = models.ManyToManyField(Blog, blank=True)

    def __str__(self):
        return '%s' % (self.name)

class Quote(models.Model):
    text = models.TextField('text', max_length=200)
    by = models.CharField ('by', max_length=50)

    def __str__(self):
        return '%s' % (self.text)

class Post(models.Model):
    author = models.ForeignKey('auth.user')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(blank=True, null=True)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

# Create your models here.
