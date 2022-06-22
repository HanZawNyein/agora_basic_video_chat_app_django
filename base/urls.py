from django.urls import path
from . import views

urlpatterns = [
    path('', views.lobby, name="lobby"),
    path('room/', views.room, name="room"),
    path('get-token/', views.getToken, name="get_token"),
    path('create-member/', views.createMember, name="create_member"),
    path('get-member/', views.getMember, name="get_member"),
]
