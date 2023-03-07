from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('room-page/<str:pk>', views.room, name='room-view')
]
