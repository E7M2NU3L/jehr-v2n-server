from django.db import models

# Create your models here.
class V2NModel(models.Model):
    notes_title = models.CharField(max_length = 200)
    notes_content = models.CharField(max_length = 1000)
