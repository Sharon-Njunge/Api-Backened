from django.db import models

# Create your models here.
class ClassPeriod(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    course = models.CharField(max_length = 20)
    class_room = models.CharField(max_length = 20)

    def __str__(self):
        return self.class_room


