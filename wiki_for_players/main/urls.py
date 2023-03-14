from django.urls import path
from . import views

from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='home'),
    path('login', views.index, name='login'),
    path('register', views.RegisterUser.as_view(), name='register'),
    path('dead_cells', views.dead_cells, name='dead_cells'),
    path('hollow_knight', views.hollow_knight, name='hollow_knight'),
    path('hollow_knight_characters', views.hollow_knight_characters, name='hollow_knight_characters'),
    path('create', views.create, name='create'),
    path('hollow_knight_characters<int:pk>', views.ArticlesDetailView.as_view(), name='article_detail'),
    path('hollow_knight_characters<int:pk>_update', views.ArticlesUpdateView.as_view(), name='article_update'),
    path('hollow_knight_characters<int:pk>_delete', views.ArticlesDeleteView.as_view(), name='article_delete')

]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

