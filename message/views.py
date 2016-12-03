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
                print(pubKey)
                pubKeyOb = bytes(pubKey, 'utf-8')
                pubKeyOb = RSA.importKey(pubKey)
                print(pubKeyOb)
                print(type(pubKeyOb))
                print(pubKeyOb.e)
                print(pubKeyOb.n)
                body = bytes(form.cleaned_data['body'], 'utf-8')
                print(body)
                body = pubKeyOb.encrypt(body, 32)
                print(body)

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

            return render_to_response('allMessages.html', {"messages": messages})
    else:
        form = searchTitleForm()
    variables = RequestContext(request, {'form': form})
    messages = []
    messages = Message.objects.filter(sender=request.user)
    return render_to_response('allMessages.html', {"messages": messages}, variables, )


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
    return render_to_response('checkMessage.html', {"messages": messages}, variables, )


@csrf_exempt
def messageHome(request):
    message = Message.objects.all()
    return render_to_response('messageHome.html', {'user': request.user})

@csrf_exempt
def detail(request, message_id):
    message = Message.objects.get(pk = message_id)
    decrypt = "nothing decrypted"
    if request.method == 'POST':
        form = decryptForm(request.POST)
        if (form.is_valid()):
            # temp = (form.cleaned_data['privateKey'])
            # print(temp)
            # temp = binascii.a2b_qp(temp.encode('latin_1'))
            # #print(temp)
            # privateKey = RSA.importKey(temp)
            # decrypted=privateKey.decrypt((str(message.message_body)))
            temp = bytes(message.message_body, 'utf-8')
            private = UserProfile.objects.get(user__username__iexact=request.user.username).privateKey
            pub = UserProfile.objects.get(user__username__iexact=request.user.username).publicKey
            #print(private)
            #privateOb = bytes(private, 'utf-8')
            #print(privateOb)
            #print(type (privateOb))
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
    if Message.objects.get(pk = message_id).delete():
        return render_to_response('messageHome.html')
    else:
        return render_to_response('messageHome.html')
