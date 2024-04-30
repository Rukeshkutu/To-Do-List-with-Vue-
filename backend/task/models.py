from django.db import models

# Create your models here.

class Task(models.Model):
    TODO = 'todo'
    DONE = 'done'

    STATUS_CHOICE = (
        (TODO, 'Todo'),
        (DONE, 'Done')
    )

    description = models.CharField(max_length=255)
    status = models.CharField(max_length=10, choices=STATUS_CHOICE, default=TODO)