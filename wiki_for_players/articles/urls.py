from django.urls import path
from . import views


urlpatterns = [
    path('', views.articles_home, name='articles_home')



]
