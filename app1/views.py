from django.shortcuts import render, get_object_or_404
from .models import Course, CourseSchedule, Student, StudentRegistration
from .forms import CourseSearchForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .models import Course, StudentRegistration
from .forms import SignUpForm, CourseSearchForm

def index(request):
    return render(request, 'app1/index.html')


def course_list(request):
    courses = Course.objects.all()
    return render(request, 'app1/course_list.html', {'courses': courses})


def course_detail(request, code):
    course = get_object_or_404(Course, code=code)
    return render(request, 'app1/course_detail.html', {'course': course})


def schedule_list(request):
    schedules = CourseSchedule.objects.all()
    return render(request, 'app1/schedule_list.html', {'schedules': schedules})


def schedule_detail(request, id):
    schedule = get_object_or_404(CourseSchedule, id=id)
    return render(request, 'app1/schedule_detail.html', {'schedule': schedule})


def student_list(request):
    students = Student.objects.all()
    return render(request, 'app1/student_list.html', {'students': students})


def student_detail(request, id):
    student = get_object_or_404(Student, id=id)
    return render(request, 'app1/student_detail.html', {'student': student})


def registration_list(request):
    registrations = StudentRegistration.objects.all()
    return render(request, 'app1/registration_list.html', {'registrations': registrations})

def registration_detail(request, id):
    registration = get_object_or_404(StudentRegistration, id=id)
    return render(request, 'app1/registration_detail.html', {'registration': registration})

def search_courses(request):
    if request.method == 'GET':
        search_form = CourseSearchForm(request.GET)
        if search_form.is_valid():
            code = search_form.cleaned_data.get('code')
            name = search_form.cleaned_data.get('name')
            instructor = search_form.cleaned_data.get('instructor')

            courses = Course.objects.all()
            if code:
                courses = courses.filter(code__icontains=code)
            if name:
                courses = courses.filter(name__icontains=name)
            if instructor:
                courses = courses.filter(instructor__icontains=instructor)

            return render(request, 'app1/course_search_results.html', {
                'form': search_form,
                'courses': courses
            })
    else:
        search_form = CourseSearchForm()

    return render(request, 'app1/course_search.html', {'form': search_form})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('search_courses')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def search_courses(request):
    if request.method == 'GET':
        form = CourseSearchForm(request.GET)
        if form.is_valid():   
            pass 
    else:
        form = CourseSearchForm()
    return render(request, 'search_courses.html', {'form': form})