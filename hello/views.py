from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, StreamingHttpResponse, FileResponse
import json
import os
from .forms import MessageForm
from .models import Message

def start_page(request):
    return render(request, 'hello/start_page.html')

def hello_world(request):
    return render(request, 'hello/hello_world.html')

def submit_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_messages')
    else:
        form = MessageForm()
    return render(request, 'message_board/submit_message.html', {'form': form})

def get_messages(request):
    if request.method == 'GET':
        name = request.GET.get('name')
        sent_messages = Message.objects.filter(sender=name).order_by('-timestamp')[:20]
        received_messages = Message.objects.filter(recipient=name).order_by('-timestamp')[:20]
        return render(request, 'message_board/get_messages.html', {
            'sent_messages': sent_messages,
            'received_messages': received_messages,
        })
    
def http_response(request):
    return HttpResponse("This is a simple HttpResponse")

def json_response(request):
    data = {'key': 'value'}
    return JsonResponse(data)

def streaming_response(request):
    def stream():
        yield "Streaming Response Line 1\n"
        yield "Streaming Response Line 2\n"

    return StreamingHttpResponse(stream(), content_type="text/plain")

def file_response(request):
    file_path = os.path.join('hello', 'static', 'files', 'example.txt')
    return FileResponse(open(file_path, 'rb'))