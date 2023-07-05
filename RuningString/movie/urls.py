from django.urls import path
from . import views

app_name = 'movie'

urlpatterns = [
    path('', views.home, name='home'),
    path('last_files/', views.last_files, name='last_files'),
    path('<str:filepath>/', views.download_file, name='download_file'),

]
