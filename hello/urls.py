from django.urls import path
from .views import (
    hello_world, submit_message, get_messages, start_page,
    http_response, http_response_redirect, http_response_permanent_redirect,
    http_response_not_modified, http_response_bad_request, http_response_not_found,
    http_response_forbidden, http_response_not_allowed, http_response_gone,
    http_response_server_error, json_response, streaming_response, file_response
)

urlpatterns = [
    path('', start_page, name='start_page'),
    path('hello/', hello_world, name='hello_world'),
    path('submit/', submit_message, name='submit_message'),
    path('messages/', get_messages, name='get_messages'),
    path('http-response/', http_response, name='http_response'),
    path('http-response-redirect/', http_response_redirect, name='http_response_redirect'),
    path('http-response-permanent-redirect/', http_response_permanent_redirect, name='http_response_permanent_redirect'),
    path('http-response-not-modified/', http_response_not_modified, name='http_response_not_modified'),
    path('http-response-bad-request/', http_response_bad_request, name='http_response_bad_request'),
    path('http-response-not-found/', http_response_not_found, name='http_response_not_found'),
    path('http-response-forbidden/', http_response_forbidden, name='http_response_forbidden'),
    path('http-response-not-allowed/', http_response_not_allowed, name='http_response_not_allowed'),
    path('http-response-gone/', http_response_gone, name='http_response_gone'),
    path('http-response-server-error/', http_response_server_error, name='http_response_server_error'),
    path('json-response/', json_response, name='json_response'),
    path('streaming-response/', streaming_response, name='streaming_response'),
    path('file-response/', file_response, name='file_response'),
]
