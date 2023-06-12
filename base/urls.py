from django.urls import path
from . import views
from . import tasks

urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', tasks.upload_file, name='upload_file'),
]