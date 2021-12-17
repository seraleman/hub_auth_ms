from django.db import models


class Role(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField("Name", max_length=50)
