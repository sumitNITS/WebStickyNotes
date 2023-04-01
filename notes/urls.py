from django.urls import path
from . import views

app_name='notes'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:note_id>/delete', views.delete, name='delete'),
    path('<int:note_id>/update', views.update, name='update'),
    path('add/', views.add, name='add')
]