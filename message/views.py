from django.shortcuts import render
from .models import Message
from .forms import *
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.template import RequestContext

# Create your views here.


def createMessage(request):
    if request.method == 'POST':
        user = request.user
        form = MessageForm(request.POST)
        message = form.instance
        if form.is_valid():

            form.save(commit=True)
            message.user_set.add(user)

        return HttpResponseRedirect('/message/')
    else:
        form = MessageForm()
    variables = RequestContext(request, {
        'form': form
    })


    return render_to_response(
        'createMessage.html',
        variables,
    )

def displayMessage(request) :
        message = Message.objects.all()
        return render_to_response('allMessages.html')