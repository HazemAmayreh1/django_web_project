from django.db import models

class Course(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    prerequisites = models.ManyToManyField('self', symmetrical=False, blank=True)
    instructor = models.CharField(max_length=100)
    capacity = models.IntegerField()
    scheduled = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class CourseSchedule(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='schedules')
    days = models.CharField(max_length=50)
    start_time = models.TimeField()
    end_time = models.TimeField()
    room_number = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.course.name} Schedule"

class Student(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class StudentRegistration(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='registrations')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='registrations')

    def __str__(self):
        return f"{self.student.name} registered for {self.course.name}"
