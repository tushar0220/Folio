from django.urls import path
from .views import home, download_file

urlpatterns = [
    path('', home, name='home'),
    path('download/',download_file, name='download_file'),

]