from django.db import models
from django.utils import timezone 
from django.core.validators import validate_email

# First create the class
    # add __str__ to the class (will be shown the contenct in the admin panel)
# Add the class to admin.py to allow manage the content in the admin panel 
# Run makemigration for the app
# Run migrate
# Check admin panel

 
class Comment(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(blank=False, validators=[validate_email], default='null')
    comment = models.TextField()
    url_name = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return '<Name: {}, ID: {}, URL_name: {}>'.format(self.name, self.id, self.url_name)


class TemporaryUser(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(blank=False, validators=[validate_email], default='null')
    password = models.CharField(max_length=64)
    date_added = models.DateTimeField(default=timezone.now)
    activation_code = models.TextField(blank=False, default='null')
    
    def __str__(self):
        return '<Name: {}, ID: {}, Email: {}>'.format(self.username, self.id, self.email)
    
class User(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(blank=False, validators=[validate_email], default='null')
    password = models.CharField(max_length=64)
    date_added = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return '<Name: {}, ID: {}, Email: {}>'.format(self.username, self.id, self.email)
