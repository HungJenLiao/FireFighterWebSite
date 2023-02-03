from django.db import models

# Create your models here.
class Emergency(models.Model):
    time = models.DateTimeField("案發日期")
    unit = models.CharField(max_length = 10)
    category = models.CharField(max_length = 10)
    detail = models.CharField(max_length = 10)
    location = models.CharField(max_length = 100)

    def __str__(self):
        return self.location

class LogRecord(models.Model):
    activate = models.CharField(max_length = 20)
    ip = models.CharField(max_length = 20)
    content = models.CharField(max_length = 50)
    member = models.CharField(max_length = 10)
    time = models.DateTimeField("紀錄時間", auto_now_add = True)
