from django.http import HttpResponse
import datetime

def some_page(request):
    html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Django App</title>
</head>
<body>
    <h1>Hello Nerds! {datetime.datetime.now()}</h1>
</body>
</html>
"""
    return HttpResponse(html)