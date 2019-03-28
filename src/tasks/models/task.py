from django.db import models
from django.conf import settings


class Task(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    done_date = models.DateTimeField()

    NEW = "NEW"
    DONE = "DONE"
    STATUS_TYPE_CHOICES = (
        (NEW, "New"),
        (DONE, "Done"),
    )
    task_status = models.CharField(max_length=4, choices=STATUS_TYPE_CHOICES, default=NEW)
