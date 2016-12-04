from django.shortcuts import render
from .models import Message
from .forms import DeleteForm, searchSenderForm, searchTitleForm, MessageForm, decryptForm
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from registration import *
from django.contrib.auth.models import User
from registration.models import UserProfile
from message.templates import *
from Crypto.PublicKey import *
from Crypto import Random
import ast
import binascii
# Create your views here.


@csrf_exempt
def createMessage(request):
    if request.method == 'POST':
        user = request.user
        form = MessageForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['encrypt'])
            #pubKey = UserProfile.objects.get(user__username__iexact=form.cleaned_data['sendToUser']).publicKey

            if form.cleaned_data['encrypt'] == True:
                print(form.cleaned_data['sendToUser'])
                pubKey = UserProfile.objects.get(user__username__iexact=form.cleaned_data['sendToUser']).publicKey
                pubKeyOb = bytes(pubKey, 'utf-8')
                pubKeyOb = RSA.importKey(pubKey)
                body = bytes(form.cleaned_data['body'], 'utf-8')
                body = pubKeyOb.encrypt(body, 32)


                message = Message.objects.create(
                    receiver=User.objects.get(username__iexact=form.cleaned_data['sendToUser']),
                    sender=user,  # User.objects.get(username__iexact=request.user),
                    message_title=form.cleaned_data['title'],
                    message_body= body

                )
            if form.cleaned_data['encrypt'] == False:
                message = Message.objects.create(
                    receiver=User.objects.get(username__iexact=form.cleaned_data['sendToUser']),
                    sender=user,  # User.objects.get(username__iexact=request.user),
                    message_title=form.cleaned_data['title'],
                    message_body=form.cleaned_data['body'],

            )

        return HttpResponseRedirect('/messageHome/')
    else:
        form = MessageForm()
    variables = RequestContext(request, {'form': form})

    return render_to_response('createMessage.html',variables,)


@csrf_exempt
def displayMessage(request):
    title = None
    if request.method == 'POST':
        form = searchTitleForm(request.POST)
        if (form.is_valid()):
            messages = []
            title = form.cleaned_data['title']

            if title != None:
                messages = Message.objects.filter(sender=request.user, message_title=title)
            else:
                messages = Message.objects.filter(sender=request.user)

            return render_to_response('allMessages.html', {'messages': messages, 'form':form})
    else:
        form = searchTitleForm()
    variables = RequestContext(request, {'form': form})
    messages = []
    messages = Message.objects.filter(sender=request.user)
    userPro = UserProfile.objects.get(user__username__iexact=request.user.username)
    userPro.sentMessagesScene= (len(messages))
    userPro.save()
    return render_to_response('allMessages.html', {'messages': messages}, variables,)


@csrf_exempt
def checkMessage(request):
    receiver = None
    messages = []
    if request.method == 'POST':
        titleForm = searchTitleForm(request.POST)
        senderForm = searchSenderForm(request.POST)
        dForm = DeleteForm(request.POST)


        if titleForm.is_valid(): #and not senderForm.is_valid():
              title = titleForm.cleaned_data['title']

              messages = Message.objects.filter(receiver=request.user, message_title=title)

              return render_to_response('checkMessage.html', {"messages": messages})

         # if senderForm.is_valid(): # and senderForm.is_valid():
         #
         #    sender = senderForm.cleaned_data['sender']
         #
         #    messages = Message.objects.filter(receiver=request.user, sender=User.objects.get(username__iexact=sender))
         #
         #    return render_to_response('checkMessage.html', {"messages": messages})

        # if titleForm.is_valid() and senderForm.is_valid():
        #
        #     title = titleForm.cleaned_data['title']
        #
        #     sender = senderForm.cleaned_data['sender']
        #
        #     messages = Message.objects.filter(receiver=request.user, sender=User.objects.get(username__iexact=sender),message_title=title)
        #
        #     return render_to_response('checkMessage.html', {"messages": messages})

    else:
        titleForm = searchTitleForm()
        senderForm = searchSenderForm()
        dFrom = DeleteForm()

    variables = RequestContext(request, {'titleForm':titleForm, 'senderForm': senderForm, 'deleteForm':DeleteForm})
    messages = []
    messages = Message.objects.filter(receiver=request.user)
    userPro = UserProfile.objects.get(user__username__iexact=request.user.username)
    userPro.recMessagesScene = (len(messages))
    userPro.save()
    return render_to_response('checkMessage.html', {"messages": messages}, variables, )


@csrf_exempt
def messageHome(request):
    userPro = UserProfile.objects.get(user__username__iexact=request.user.username)
    recMessage = []
    sentMessage =[]
    sentMessage = Message.objects.filter(sender=request.user)
    recMessage = Message.objects.filter(receiver=request.user)
    oldR = (len(recMessage))
    oldS = (len(sentMessage))
    newR = str((len(recMessage) - int(userPro.recMessagesScene)))
    newS = str((len(sentMessage) - int(userPro.sentMessagesScene)))
    if(int(newR) < 0):
        newR = 0
    if(int(newS) < 0):
        newS = 0

    return render_to_response('messageHome.html', {'user': request.user, 'userPro': userPro, 'newR':newR, 'newS':newS, 'oldR':oldR, 'oldS':oldS})

@csrf_exempt
def detail(request, message_id):
    message = Message.objects.get(pk = message_id)
    decrypted = "nothing decrypted"
    if request.method == 'POST':
        form = decryptForm(request.POST)
        if (form.is_valid()):
            temp = bytes(message.message_body, 'utf-8')
            private = UserProfile.objects.get(user__username__iexact=request.user.username).privateKey
            pub = UserProfile.objects.get(user__username__iexact=request.user.username).publicKey
            privKeyOb = RSA.importKey(private)
            body = bytes(message.message_body, 'utf-8')
            priv = privKeyOb.decrypt(ast.literal_eval(str(message.message_body)))
            print(priv)
            decrypted = priv
    else:
        form = decryptForm()
        decrypted = "nothing decrypted"
    return render_to_response('messageDetail.html', {'message': message, 'form':form, 'decrypt':decrypted})


@csrf_exempt
def deleteMessage(request, message_id):
    userPro = UserProfile.objects.get(user__username__iexact=request.user.username)
    if Message.objects.get(pk = message_id).sender == request.user:
        userPro.recMessagesScene=str(int(userPro.recMessagesScene)-1)
    else:
        userPro.sentMessagesScene=str(int(userPro.sentMessagesScene)-1)
    if Message.objects.get(pk = message_id).delete():
        return render_to_response('messageDeleted.html')
    else:
        return render_to_response('messageDeleted.html')



@csrf_exempt
def messageDeleted(request):
        return render_to_response('messageDeleted.html')
