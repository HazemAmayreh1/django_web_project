from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Course

class CourseSearchForm(forms.Form):
    code = forms.CharField(required=False, label='Course Code')
    name = forms.CharField(required=False, label='Course Name')
    instructor = forms.CharField(required=False, label='Instructor Name')
class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )

class CourseSearchForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('code', 'name', 'instructor', )
