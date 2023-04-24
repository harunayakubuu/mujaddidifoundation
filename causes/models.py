from django.db import models


class Cause(models.Model):
    title = models.CharField(max_length = 50)
    
