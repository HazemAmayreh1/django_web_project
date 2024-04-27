
from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app1/', include('app1.urls')),  
    path('', include('app1.urls')), 
    
]
