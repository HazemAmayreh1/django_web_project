from django.urls import path
from . import views
from .views import search_courses


urlpatterns = [

    path('', views.index, name='index'), 
    
    path('courses/', views.course_list, name='course_list'),
    path('courses/<str:code>/', views.course_detail, name='course_detail'),
    
    path('schedules/', views.schedule_list, name='schedule_list'),
    path('schedules/<int:id>/', views.schedule_detail, name='schedule_detail'),
    
    path('students/', views.student_list, name='student_list'),
    path('students/<int:id>/', views.student_detail, name='student_detail'),
    
    path('registrations/', views.registration_list, name='registration_list'),
    path('registrations/<int:id>/', views.registration_detail, name='registration_detail'),

    path('signup/', views.signup, name='signup'),
    
    path('courses/search/', views.search_courses, name='search_courses'),

]


