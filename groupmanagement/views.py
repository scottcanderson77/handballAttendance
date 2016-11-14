from django.shortcuts import render
# views.py
from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.models import User, Group

# Create your views here.
def displayUsers(request):
    users = User.objects.all()
    current_user = request.user.username;
    return render(request, 'groupmanagement/allusers.html', {'users' : users, 'current_user' : current_user})