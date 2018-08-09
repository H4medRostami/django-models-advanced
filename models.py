#models.py
from django.db import models

class bookmanager(models.manager):
  def title_count(self, keyword):
    return self.fiter(title__icontains=keyword).count()
 
 class book(models.Model):
 title=models.CharField(max_length=100)
 publication_date=models.DateField()
 objects=bookmanager()
