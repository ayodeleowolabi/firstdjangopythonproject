from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    # path('new', views.new, name='new'),
    path('about/', views.about, name='about'),
    path('characters/', views.character_index, name='character-index'),
      path('character/<int:character_id>/add-gamesession',
         views.add_gamesession,
         name='add-gamesession'
         ),
    path('characters/<int:character_id>/', views.character_detail, name='character-detail'),
    path('characters/create/', views.CharacterCreate.as_view(), name='character-create'), 
    path('character/<int:pk>/update/', views.CharacterUpdate.as_view(), name='character-update'),
    path('characters/<int:pk>/delete/', views.CharacterDelete.as_view(), name='character-delete'),
    
    ]