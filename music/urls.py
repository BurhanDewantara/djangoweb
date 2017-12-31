from django.urls import path
from . import views

app_name = 'music'
urlpatterns = [
    path('',views.AlbumListView.as_view(), name = "index"),
    
    # /1
    path('<pk>/',views.AlbumDetailView.as_view(), name = "detail"),
    
    # album/add
    path('album/add/', views.AlbumCreateView.as_view(), name = 'album-add'),
    
    # album/2
    path('album/<pk>/', views.AlbumUpdateView.as_view(), name = 'album-edit'),

    # # album/2/favorite
    # path('album/<pk>/favorite', views.AlbumDeleteView.as_view(), name = 'album-favorite'),
    
    # album/2/favorite
    path('album/<pk>/delete', views.AlbumDeleteView.as_view(), name = 'album-delete'),
    
]