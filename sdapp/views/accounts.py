from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.template import RequestContext, context
from django.http import HttpResponse
from django.template import loader

@login_required
def profile(request):
    template = loader.get_template('sdapp/accounts/profile.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context, request))
