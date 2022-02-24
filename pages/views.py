from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Hello World</h1>")
    my_context = {
        "my_text": "This is about us",
        "my_number": 1234567,
        "my_list": [123, 234, 453]
    }
    return render(request, "home.html", my_context)