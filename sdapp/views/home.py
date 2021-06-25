from sdapp.forms import LoginForm
from django.views import View
from django.shortcuts import render

class Home(View):
    def get(self, request):

        loginf = LoginForm()
        context = {'name': 'Administrator', 'l': loginf}

        return render(request, 'sdapp/index.html', context)    
