# views.py
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User, Group
from django.http import HttpResponse
import json


# Create your views here.
def displayUsers(request, placeholder):
    users = User.objects.all()
    page_path = request.get_full_path()
    lastOccurence = page_path.rfind('/')
    g_id = int(page_path[lastOccurence+1:])
    g_user_set = Group.objects.get(id=g_id).user_set.all()
    current_user = request.user
    print(g_user_set)
    return render(request, 'groupmanagement/allusers.html', {'users' : users, 'current_user' : current_user, 'g_id' : g_id, 'groupUsers' : g_user_set})

def viewGroups(request):
    current_user = request.user
    all_groups = Group.objects.all()
    if not current_user.is_superuser:
        all_groups = current_user.groups.all()

    return render(request, 'groupmanagement/yourgroups.html', {'groups' : all_groups})

def groupActionsView(request, placeholder):
    page_path = request.get_full_path()
    lastOccurence = page_path.rfind('/')
    g_id = int(page_path[lastOccurence+1:])
    g = Group.objects.get(id=g_id)
    return render(request, 'groupmanagement/groupActions.html', {'name' : g.name, 'g_id' : g_id})

@csrf_exempt
def addMember(request):
    username = request.POST.get('username')
    groupID = request.POST.get('groupID')
    user = User.objects.get(username=username)
    group = Group.objects.get(id=groupID)
    group.user_set.add(user)
    return HttpResponse(json.dumps({"g_id" : groupID}), status=200, content_type="application/json")

@csrf_exempt
def removeMember(request):
    username = request.POST.get('username')
    groupID = request.POST.get('groupID')
    user = User.objects.get(username=username)
    group = Group.objects.get(id=groupID)
    group.user_set.remove(user)
    return HttpResponse(json.dumps({"g_id" : groupID}), status=200, content_type="application/json")