from django.shortcuts import render
from .models import Message
from .forms import *
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from registration import *
from message.templates import *

# Create your views here.


@csrf_exempt
def createMessage(request):
    if request.method == 'POST':
        user = request.user
        form = MessageForm(request.POST)
        if form.is_valid():

            message = Message.objects.create(
                sender =  request.user,#User.objects.get(username__iexact=request.user),
                receiver=User.objects.get(username__iexact=form.cleaned_data['sendToUser']),
                message_title = form.cleaned_data['title'],
                message_body = form.cleaned_data['body'],
            )

        return HttpResponseRedirect('/messageHome/')
    else:
        form = MessageForm()
    variables = RequestContext(request, {
        'form': form
    })

    return render_to_response(
        'createMessage.html',
        variables,
    )


@csrf_exempt
def displayMessage(request):
    receiver = None
    if request.method =='POST':
        form = searchTitleForm(request.POST)
        if(form.is_valid()):
           messages = []
           title = form.cleaned_data['title']

           if (title != None):
               messages = Message.objects.filter(sender=request.user, message_title=title)
           else:
               messages = Message.objects.filter(sender=request.user)

           return render_to_response('allMessages.html', {"messages": messages})
    else:
        form = searchTitleForm()
    variables = RequestContext(request, {'form': form})
    messages = []
    messages = Message.objects.filter(sender=request.user)
    return render_to_response('allMessages.html', {"messages": messages}, variables,)


@csrf_exempt
def checkMessage(request):
    receiver = None
    if request.method == 'POST':
        form = searchTitleForm(request.POST)
        if (form.is_valid()):
            messages = []
            title = form.cleaned_data['title']

            if (title != None):
                messages = Message.objects.filter(sender=request.user, message_title=title)
            else:
                messages = Message.objects.filter(reciever=request.user)

            return render_to_response('checkMessage.html', {"messages": messages})
    else:
        form = searchTitleForm()
    variables = RequestContext(request, {'form': form})
    messages = []
    messages = Message.objects.filter(receiver=request.user)
    return render_to_response('checkMessage.html', {"messages": messages}, variables, )


@csrf_exempt
def messageHome(request):
        message = Message.objects.all()
        return render_to_response('messageHome.html')