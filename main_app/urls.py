from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('characters/', views.character_index, name='character-index'),
    path('characters/<int:character_id>/', views.character_detail, name='character-detail'),
]