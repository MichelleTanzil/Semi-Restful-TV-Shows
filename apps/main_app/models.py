from __future__ import unicode_literals
from django.db import models
from datetime import date, datetime

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors['title'] = "Title name should be at least 2 characters long"
        if Show.objects.filter(title = postData['title']).exists():
            errors['title'] = "This TV show already exists"
        if len(postData['network']) < 3:
            errors['network'] = "Network name should be at least 3 characters long"
        if len(postData['description']) < 10 and len(postData['description']) > 0:
            errors['desc'] = "The description should be at least 10 characters long"
        if len(postData['release_date']) == 0 or datetime.strptime(postData['release_date'], '%Y-%m-%d') > datetime.today():
            errors['release_date'] = "The release date should be a valid date and in the past"
        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateTimeField()
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()

    def __repr__(self):
        return f"<Show Object: {self.id} {self.title} {self.network} {self.release_date}>"
