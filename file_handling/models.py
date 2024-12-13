from django.db import models
import pandas as pd




# models.py
from django.db import models

class YourModel(models.Model):
    file = models.FileField(upload_to='uploads/')
    # Add other fields as needed

class Meta:
    db_table = 'Uploads'