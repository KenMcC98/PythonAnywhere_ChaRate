from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

#class Movie(models.Model):
#    name = models.CharField(max_length=128, unique = True)
#    ID = models.IntegerField(max_length=128, unique = True)
#    genre = models.CharField(max_length=16)
#    slug = models.SlugField(unique=True)
#
#    def save(self, *args, **kwargs):
#        seld.slug =slugify(self.name)
#        super(Movie, self).save(*args, **kwargs)
#
#    def __str__(self):
#        return self.name
#
#
#class TV(models.Model):
#    name = models.CharField(max_length=128, unique = True)
#    ID = models.IntegerField(max_length=128, unique = True)
#    genre = models.CharField(max_length=16)
#    slug = models.SlugField(unique=True)
#
#    def save(self, *args, **kwargs):
#        seld.slug =slugify(self.name)
#        super(TV, self).save(*args, **kwargs)
#
#    class Meta:
#        verbose_name_plural = 'TV Shows'
#
#    def __str__(self):
#        return self.name
#
#
#class Character(models.Model):
#    name = models.CharField(max_length=128, unique = True)
#    ID = models.IntegerField(unique = True)
#    likes = models.IntegerField(default=0)
#    comments = [{"user": "****"},] 
#    picture = models.ImageField(upload_to='character_images', blank=True)
#
#    def __str__(self): 
#        return self.name

                

class UserProfile(models.Model):
    username = models.CharField(max_length=16, unique = True)

    def __str__(self):
        return self.user.username

