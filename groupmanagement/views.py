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

def viewGroups(request):
    current_user = request.user
    all_groups = current_user.groups.all()
    return render(request, 'groupmanagement/yourgroups.html', {'groups' : all_groups})

def groupActionsView(request, placeholder):
    page_path = request.get_full_path()
    lastOccurence = page_path.rfind('/')
    g_id = int(page_path[lastOccurence+1:])
    g = Group.objects.get(id=g_id)
    return render(request, 'groupmanagement/groupActions.html', {'name' : g.name})
