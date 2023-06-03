from django.db import models

class Schedule(models.Model):
    # owner_user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    # assigned_to_user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()