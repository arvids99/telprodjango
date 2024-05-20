from django.http import HttpResponse

def hello_world(request):
    html = """
    <html>
    <head>
        <title>Hello World</title>
        <style>
            body { font-family: Arial, sans-serif; }
            h1 { color: blue; }
        </style>
        <script>
            function showAlert() {
                alert('Hello from JavaScript!');
            }
        </script>
    </head>
    <body>
        <h1>Hello, World!</h1>
        <button onclick="showAlert()">Click me</button>
    </body>
    </html>
    """
    return HttpResponse(html)
