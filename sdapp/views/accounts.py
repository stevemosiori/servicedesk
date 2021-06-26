from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

@login_required
def profile(request):
    cxt = RequestContext(request)
    return render(request, 'sdapp/accounts/profile.html')
