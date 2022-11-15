from django.urls import path
from . import views
from exploration.dash_apps.finished_apps import simpleexample

app_name='exploration'

urlpatterns = [
    path('',views.dashboard_view,name='dashboard')
]
