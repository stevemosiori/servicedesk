from django.shortcuts import render

def login(request):
    return render(request, 'sdapp/auth/login.html', {'name': 'Steve'}) 