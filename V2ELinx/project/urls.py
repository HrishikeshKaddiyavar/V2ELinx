"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name='Index'),
    # path('About', views.About, name='About'),
    path('StaffSignIn', views.StaffSignIn, name='StaffSignIn'),
    path('StaffSignUp', views.StaffSignUp, name='StaffSignUp'),
    path('AddNewStudent', views.AddNewStudent, name='AddNewStudent'),
    path('Attendance', views.Attendance, name='Attendance'),
    path('UpdateStudentDetails', views.UpdateStudent, name='UpdateStudent'),
    path('RemoveStudent', views.RemoveStudent, name='RemoveStudent'),
    path('GetStudentDetails', views.GetStudentDetails, name='GetStudentDetails'),
    path('GetStudentDetails/PDF', views.GetStudentDetailsPDF, name='GetStudentDetailsPDF'),
    path('SetMarks', views.SetMarks, name='SetMarks'),
    path('UpdateMarks', views.UpdateMarks, name='UpdateMarks'),
    path('GetMarks', views.GetMarks, name='GetMarks'),
    path('GetMarks/PDF', views.GetMarksPDF, name='GetMarksPDF'),
    path('Ranks', views.Ranks, name='Ranks'),
    path('Ranks/PDF', views.RanksPDF, name='RanksPDF'),
    path('Contact', views.Contact, name='Contact'),
    # path('UserManual', views.UserManual, name='UserManual'),
    path('admin/', admin.site.urls),
]
