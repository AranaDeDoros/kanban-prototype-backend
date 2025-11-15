from django.db import models
from django.conf import settings
from projects.models import Project

class Task(models.Model):
    STATUS_CHOICES = [
        ('backlog', 'Backlog'),
        ('wip', 'In Progress'),
        ('done', 'Completed'),
    ]

    PRIORITIES = [
        ('high', 'High'),
        ('regular', 'Regular'),
        ('low', 'Low'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='backlog')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='tasks_assigned'
    )
    priority = models.CharField(max_length=20, choices=STATUS_CHOICES, default='regular') #arrows, icons
    estimate_points = models.IntegerField(default=1) #regular input
    acceptance_criteria = models.TextField(default='', help_text='Acceptance Criteria') #available on click

    def __str__(self):
        return self.title