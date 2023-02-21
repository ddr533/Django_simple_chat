from django.urls import path

from . import views

app_name = 'rooms'

urlpatterns = [
    path('', views.get_room_list, name='room_list'),
    path('<slug:room_slug>', views.get_room_detail, name='room_detail'),
]
