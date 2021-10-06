from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('chat/<str:pk>/', views.chat, name="chat"),

    path('create_chat/<str:pk>/', views.create_chat, name="create_chat"),
    path('update_chat/<str:pk>/', views.update_chat, name="update_chat"),
    path('delete_chat/<str:pk>/', views.delete_chat, name="delete_chat"),

    path('chatter/<str:pk>/', views.chatter, name="chatter"),

]
