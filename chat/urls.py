from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.index, name="chat-index"),
    path('<str:room_name>/', views.room, name="room"),

]
