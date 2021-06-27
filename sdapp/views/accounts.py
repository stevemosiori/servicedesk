from django.shortcuts import render
from django.template import RequestContext, Template
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    return render(request, 'sdapp/accounts/profile.html', {
        'view_reqs': ['pwstrength']
    })
