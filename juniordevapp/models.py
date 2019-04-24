from django.db import models

# Create your models here.
class Teacher(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    e_mail = models.EmailField(max_length=20)
    
    def __str__(self):
        return self.first_name

    def save_teacher(self):
        self.save()

    def delete_teacher(self):
        self.delete()

class Student(models.Model):
    user_name = models.CharField(max_length =60)
    full_name = models.CharField(max_length =60)
    age = models.CharField(max_length =12)
   
    def __str__(self):
        return self.name

    def save_student(self):
        self.save()  
    def delete_student(self):
        self.delete()
          

class Parent(models.Model):
    user_name = models.CharField(max_length =60)
    full_name = models.CharField(max_length =60)
    age = models.CharField(max_length =12)
   
    def __str__(self):
        return self.name

    def save_parent(self):
        self.save()         
    def delete_parent(self):
        self.delete()
    
class School(models.Model):
    description = models.CharField(max_length=30)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)

    def __str__(self):
        return self.description

   


