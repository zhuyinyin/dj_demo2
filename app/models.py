from django.db import models

# Create your models here.


class User(models.Model):
    uid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32, default='')


class Produce(models.Model):
    pid = models.AutoField(primary_key=True)
    p_name = models.CharField(max_length=32)
    p_describe = models.CharField(max_length=32)
    p_start = models.DateTimeField(auto_now_add=True)
    p_stop = models.DateTimeField(auto_now=True)
    p_price = models.DecimalField(max_digits=6, decimal_places=2)


class Record(models.Model):
    rid = models.AutoField(primary_key=True)
    r_time = models.DateTimeField(auto_now=True)
    r_price = models.DecimalField(max_digits=10, decimal_places=2)
    r_person = models.CharField(max_length=32)
    p_id = models.IntegerField()
