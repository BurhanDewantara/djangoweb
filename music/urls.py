from django.urls import path
from . import views

app_name = 'music'
urlpatterns = [
    path('',views.AlbumListView.as_view(), name="index"),
    path('<pk>/',views.AlbumDetailView.as_view(), name="detail")
]