# models.py
from django.db import models

class StudentDetail(models.Model):
    registerNo = models.TextField(primary_key=True)
    studentName = models.TextField()
    standard = models.IntegerField()
    marks = models.IntegerField()
    attendance = models.TextField()
    result = models.TextField()

class Class8Ranks(models.Model):
    rank = models.IntegerField()
    registerNo = models.TextField(primary_key=True)
    studentName = models.TextField()
    standard = models.IntegerField()
    marks = models.IntegerField()

class Class9Ranks(models.Model):
    rank = models.IntegerField()
    registerNo = models.TextField(primary_key=True)
    studentName = models.TextField()
    standard = models.IntegerField()
    marks = models.IntegerField()

class Class10Ranks(models.Model):
    rank = models.IntegerField()
    registerNo = models.TextField(primary_key=True)
    studentName = models.TextField()
    standard = models.IntegerField()
    marks = models.IntegerField()

class SchoolRanks(models.Model):
    rank = models.IntegerField()
    registerNo = models.TextField(primary_key=True)
    studentName = models.TextField()
    standard = models.IntegerField()
    marks = models.IntegerField()
