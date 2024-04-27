from django.contrib import admin
from .models import Course, CourseSchedule, Student, StudentRegistration

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'instructor', 'capacity', 'scheduled')
    search_fields = ('name', 'instructor')
    list_filter = ('scheduled',)

@admin.register(CourseSchedule)
class CourseScheduleAdmin(admin.ModelAdmin):
    list_display = ('course', 'days', 'start_time', 'end_time', 'room_number')
    list_filter = ('days', 'room_number')
    search_fields = ('course__name',)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')
    search_fields = ('name', 'email')

@admin.register(StudentRegistration)
class StudentRegistrationAdmin(admin.ModelAdmin):
    list_display = ('student', 'course')
    search_fields = ('student__name', 'course__name')
    list_filter = ('course',)
