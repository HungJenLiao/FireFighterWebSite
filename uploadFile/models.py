from django.db import models

# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length = 10)

    def __str__(self):
        return self.name

class Emergency(models.Model):
    time = models.DateTimeField("案發日期") #日期
    car = models.CharField(max_length = 10) #車輛
    # car = models.ForeignKey(Car, blank = True, null = True, on_delete = models.CASCADE)
    detail = models.CharField(max_length = 10)  #內容(急病or車禍...)
    location = models.CharField(max_length = 100)   #地點
    status = models.CharField(max_length = 1)   #是否需要修改

class LogRecord(models.Model):
    activate = models.CharField(max_length = 20)
    ip = models.CharField(max_length = 20)
    content = models.CharField(max_length = 50)
    member = models.CharField(max_length = 10)
    time = models.DateTimeField("紀錄時間", auto_now_add = True)