from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Carrers(models.Model):
    id = models.AutoField(primary_key=True,db_column='idcarrers')
    name_carrer = models.CharField(max_length=200,db_column='name_carrer')
    class Meta:
        db_table = 'carrers'

class Period(models.Model):
    id = models.AutoField(primary_key=True,db_column='idperiod')
    period_description = models.CharField(max_length=100,db_column='period_description')
    class Meta:
        db_table = 'periods'

class Group(models.Model):
    id = models.AutoField(primary_key=True, db_column='idgroup')  
    group_name = models.CharField(max_length=100, db_column='group_name')
    max_capacity_students = models.IntegerField(default=40,db_column='max_capacity_students')
    fk_period = models.ForeignKey(Period,on_delete=models.CASCADE,db_column='fk_period',default=1)
    fk_carrer = models.ForeignKey(Carrers, on_delete=models.CASCADE,db_column='fk_carrer')
    class Meta:
        db_table = 'groups'

class Course(models.Model):
    id = models.AutoField(primary_key=True,db_column='idcourse')
    type_course = models.CharField(max_length=200,db_column='type_course')
    class Meta:
        db_table='course'

class Activities(models.Model):
    id = models.AutoField(primary_key=True, db_column='idactivities')
    title = models.CharField(max_length=100, db_column='title')
    descriptions = models.TextField(db_column='description')
    date_activities = models.DateField(db_column='date_activities')
    completed = models.BooleanField(db_column='completed')
    color = models.CharField(max_length=50,db_column='color')
    fk_user = models.ForeignKey(User, on_delete=models.CASCADE, db_column='fk_user')

    class Meta:
        db_table = 'activities'
class Students(models.Model):
    id = models.AutoField(primary_key=True,db_column='idstudents')
    name = models.CharField(max_length=200,db_column='name')
    app = models.CharField(max_length=200,db_column='app')
    apm = models.CharField(max_length=200,db_column='apm')
    student_id = models.CharField(max_length=100,db_column='student_id')
    class Meta:
        db_table='students'

class GroupCourseUser(models.Model):
    id = models.AutoField(primary_key=True,db_column='idGroupCourseUser')
    fk_group = models.ForeignKey(Group,on_delete=models.CASCADE,db_column='fk_group')
    fk_course = models.ForeignKey(Course,on_delete=models.CASCADE,db_column='fk_course')
    fk_user = models.ForeignKey(User,on_delete=models.CASCADE,db_column='fk_user')
    class Meta:
        db_table='groupcourseuser'

class GroupCourseUserStudents(models.Model):
    id = models.AutoField(primary_key=True,db_column='idGroupCourseUserStudent')
    fk_group = models.ForeignKey(Group,on_delete=models.CASCADE,db_column='fk_group')
    fk_course = models.ForeignKey(Course,on_delete=models.CASCADE,db_column='fk_course')
    fk_user = models.ForeignKey(User,on_delete=models.CASCADE,db_column='fk_user')
    fk_students = models.ForeignKey(Students,on_delete=models.CASCADE,db_column='fk_student')
    class Meta:
        db_table='groupcourseuserstudents'

class Attendance(models.Model):
    id = models.AutoField(primary_key=True,db_column='idattendance')
    attendance = models.IntegerField(db_column='attendance')
    fk_group_course_user_student = models.ForeignKey(GroupCourseUserStudents,on_delete=models.CASCADE,db_column='fk_group_course_user_student')
    class Meta:
        db_table='attendance'

