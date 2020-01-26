from django.db import models
import uuid


class School(models.Model):
    name = models.CharField(max_length=20)
    max_students = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    identification = models.UUIDField(default=uuid.uuid4, db_index=True, unique=True)
    school = models.ForeignKey(School, on_delete=models.SET_NULL, null=True)
