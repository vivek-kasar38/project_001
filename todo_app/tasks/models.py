from django.db import models

class Task(models.Model):
    title =  models.CharField(max_length=200)
    description = models.TextField(blank=True)
    due_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.title

