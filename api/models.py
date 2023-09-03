from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Group(models.Model):
    id = models.AutoField(primary_key=True, db_column='idgroup')  
    group_name = models.CharField(max_length=100, db_column='group_name')
    class Meta:
        db_table = 'group'


class Activities(models.Model):
    id = models.AutoField(primary_key=True, db_column='idactivities')
    title = models.CharField(max_length=100, db_column='title')
    descriptions = models.TextField(db_column='description')
    date_activities = models.DateField(db_column='date_activities')
    completed = models.BooleanField(db_column='completed')
    color = models.CharField(max_length=50,db_column='color',default='text-warning')
    fk_user = models.ForeignKey(User, on_delete=models.CASCADE, db_column='fk_user')

    class Meta:
        db_table = 'activities'


