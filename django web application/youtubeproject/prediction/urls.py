from django.urls import path
from . import views
from prediction.dash_apps.finished_apps import importance

app_name='prediction'

urlpatterns = [
    path('',views.ml_view,name='ml')
]
