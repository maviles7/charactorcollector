from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('characters/', views.character_index, name='character-index'),
    path('characters/create/', views.CharacterCreate.as_view(), name='character-create'),
    path('characters/<int:character_id>/',views.character_detail, name='character-detail'),
    path('characters/<int:pk>/update', views.CharacterUpdate.as_view(), name='character-update'),
    path('characters/<int:pk>/delete', views.CharacterDelete.as_view(), name='character-delete'),
    path('characters/<int:character_id>/add-name/', views.add_name, name='add-name'),
    path('powers/create/', views.PowerCreate.as_view(), name='power-create'),
    path('powers/<int:pk>', views.PowerDetail.as_view(), name='power-detail'),
    path('powers/', views.PowerList.as_view(), name='power-index'),
    path('powers/<int:pk>/update', views.PowerUpdate.as_view(), name='power-update'),
    path('powers/<int:pk>/delete', views.PowerDelete.as_view(), name='power-delete'),
]