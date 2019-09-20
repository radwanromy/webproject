from django.db import models

# 01
class Computer_Science(models.Model):
    Software = models.CharField(max_length=250)
    Name = models.CharField(max_length=500)
    Tool = models.CharField(max_length=100)
    Project_Logo = models.CharField(max_length=1000)

    def __str__(self):
        return self.Name + ' - ' + self.Software

class Student(models.Model):
    Project_Name = models.ForeignKey(Computer_Science,on_delete=models.CASCADE, null=True)
    University = models.CharField(max_length=500)
    Department = models.CharField(max_length=500)
    Semester = models.CharField(max_length=500)
    Student_Or_Group_Name = models.CharField(max_length=500)


    def __str__(self):
        return self.Student_Or_Group_Name




