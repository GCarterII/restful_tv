from django.db import models
import datetime

class ShowManager(models.Manager):
    def input_vaildator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors['title'] = "Show's title must be at least 2 characters"
        if len(postData['network']) < 3:
            errors['network'] = "Network must be at least 3 characters"
        if datetime.datetime(postData['release_date']) > datetime.datetime.now():
            errors['release_date'] = "Pre-release shows are not accepted on this site"
        if len(postData['desc']) > 0:
            if len(postData['desc']) < 10:
                errors['desc'] = "Description, if there is one, must be at least 10 characters"
        return errors


#creating class for TV shows
class Show(models.Model):
    title = models.CharField(max_length=100)
    network = models.CharField(max_length=100)
    desc = models.TextField()
    release_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()





# Create your models here.
