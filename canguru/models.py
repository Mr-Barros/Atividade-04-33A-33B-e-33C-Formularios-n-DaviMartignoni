from django.db import models


class Comment(models.Model):
  title = models.CharField(max_length = 100)
  body = models.CharField(max_length = 300)
  date = models.DateField()
  likes = models.IntegerField()
  dislikes = models.IntegerField()

class LegendaryKangaroo(models.Model):
  title = models.CharField(max_length = 100)
  killcount = models.IntegerField()
  description = models.CharField(max_length = 1000)
  last_seen = models.DateField()

class KangarooType(models.Model):
  title = models.CharField(max_length = 30)
  sci_name = models.CharField(max_length = 30)
  length = models.FloatField()
  weight = models.IntegerField()
