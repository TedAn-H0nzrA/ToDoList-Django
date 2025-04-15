from django.db import models

class Task(models.Model):
    STATUS_CHOICES = [
        ('not_started', 'Not Started'),
        ('in_progress', 'In Progress'),
        ('finished', 'Finished'),
    ]

    title = models.CharField(max_length = 200)
    description = models.TextField(blank = True)
    status = models.CharField(max_length = 20, choices = STATUS_CHOICES, default = 'not_started')
    create_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title
