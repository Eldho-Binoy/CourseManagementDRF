"""
URL configuration for CourseManagerAPI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create',views.CreateCourse.as_view()),
    path('list',views.ListCourse.as_view()),
    path('update/<int:id>',views.UpdateCourse.as_view()),
    path('partialupdate/<int:id>',views.PartialUpdateCourse.as_view()),
    path('delete/<int:id>',views.DeleteCourse.as_view()),
    path('retrieve/<int:id>',views.RetrieveCourse.as_view()),

]
