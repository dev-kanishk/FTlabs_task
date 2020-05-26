from django.db import models
from accounts.models import User



class activity_period(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    user = models.ForeignKey(User, related_name='activity_periods',  on_delete=models.CASCADE)

    def __str__(self):
        to_display = str(self.start_time) + " to " + str(self.end_time)
        return to_display


