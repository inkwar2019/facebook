from django.db import models


class MyUser(models.Model):
    id = models.AutoField(primary_key=True, default=0)
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=10)
