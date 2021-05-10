from django.urls import path, include
from home.views import homeview

urlpatterns = [
    path('', homeview, name='HomeView')
]