from django.urls import path
from . import views

app_name="memalloc"

urlpatterns = [
    path('', views.index, name='index'),
]