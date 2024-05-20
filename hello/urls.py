from django.urls import path
from .views import hello_world, submit_message, get_messages

urlpatterns = [
    path('', hello_world, name='hello_world'),
    path('submit/', submit_message, name='submit_message'),
    path('messages/', get_messages, name='get_messages'),
]
