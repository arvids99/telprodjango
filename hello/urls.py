from django.urls import path
from .views import hello_world, submit_message, get_messages, start_page, http_response, json_response, streaming_response, file_response


urlpatterns = [
    path('', start_page, name='start_page'),
    path('hello/', hello_world, name='hello_world'),
    path('submit/', submit_message, name='submit_message'),
    path('messages/', get_messages, name='get_messages'),
    path('http-response/', http_response, name='http_response'),
    path('json-response/', json_response, name='json_response'),
    path('streaming-response/', streaming_response, name='streaming_response'),
    path('file-response/', file_response, name='file_response'),
]
