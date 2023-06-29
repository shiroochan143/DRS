"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from myapp import views


urlpatterns = [
    path('dashboard/', views.dashboard_index, name='dashboard_index'),
    path('dashboard/create/', views.dashboard_create, name='dashboard_create'),
    path('dashboard/view/', views.dashboard_view, name='dashboard_view'),
    path('dashboard/update/', views.dashboard_update, name='dashboard_update'),
    path('dashboard/patient-record', views.patient_record_view, name='patient_record_view'),
    path('dashboard/appointment-schedule', views.appointment_schedule_view, name='appointment_schedule_view'),
    path('dashboard/appointment-schedule/today', views.appointment_schedule_view_present, name='appointment_schedule_view_present'),
    path('dashboard/appointment-schedule/<int:pk>/', views.appointment_schedule_detail, name='appointment_schedule_detail'),
    path('dashboard/update/appointment-schedule/<int:pk>', views.appointment_schedule_update, name='appointment_schedule_update'),
    path('dashboard/create/appointment-schedule', views.appointment_schedule_create, name='appointment_schedule_create'),
    path('dashboard/search/appointment-schedule', views.appointment_schedule_search, name='appointment_schedule_search'),
    path('dashboard/search/appointment-schedule/name', views.appointment_schedule_search_name, name='appointment_schedule_search_name'),
    path('dashboard/search/appointment-schedule/date', views.appointment_schedule_search_date, name='appointment_schedule_search_date'),
    path('dashboard/<int:pk>/', views.patient_record_detail, name='patient_record_detail'),
    path('dashboard/update/<int:pk>', views.patient_record_update, name='patient_record_update'),
    #path('dashboard/search/patient-record', views.patient_record_search, name='patient_record_search'),
    path('dashboard/create/patient-record', views.patient_record_create, name='patient_record_create'),

]
