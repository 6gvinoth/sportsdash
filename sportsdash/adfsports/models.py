from django.db import models

# Create your models here.

class TeamScore(models.Model):
    TeamMatch = models.CharField( db_column='TeamMatch', max_length=100)  # Field name made lowercase.
    Sports = models.CharField(db_column='Sports', max_length=100)  # Field name made lowercase.
    Point = models.IntegerField(db_column='Point')  # Field name made lowercase.
    Wonby = models.CharField(db_column='Wonby', max_length=10)  # Field name made lowercase.
    Lossby = models.CharField(db_column='Lossby', max_length=10) 
    class Meta:
        managed = False
        db_table = 'teamsscore'
        
