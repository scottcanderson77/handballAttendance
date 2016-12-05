# views.py
from django import forms
from django import views
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from .forms import GroupingForm
from reports.models import *
from groupmanagement.models import GroupReports
import json
from django.template import RequestContext
from django.contrib.auth.decorators import login_required



# Create your views here.

def displayUsers(request, placeholder):
    users = User.objects.all()
    page_path = request.get_full_path()
    lastOccurence = page_path.rfind('/')
    g_id = int(page_path[lastOccurence+1:])
    g_user_set = Group.objects.get(id=g_id).user_set.all()
    current_user = request.user
    # print(g_user_set)
    return render(request, 'groupmanagement/allusers.html', {'users' : users, 'current_user' : current_user, 'g_id' : g_id, 'groupUsers' : g_user_set})


@csrf_exempt
def viewGroups(request):
    current_user = request.user
    all_groups = Group.objects.all()
    if not current_user.is_superuser:
        all_groups = current_user.groups.all()

    return render(request, 'groupmanagement/yourgroups.html', {'groups': all_groups})


@csrf_exempt
def groupActionsView(request, placeholder):
    page_path = request.get_full_path()

    lastOccurence = page_path.rfind('/')
    g_id = int(page_path[lastOccurence + 1:])
    g = Group.objects.get(id=g_id)
    return render(request, 'groupmanagement/groupActions.html', {'name': g.name, 'g_id': g_id})


@csrf_exempt
def addMember(request):
    username = request.POST.get('username')
    # print(username)
    groupID = request.POST.get('groupID')
    # print(groupID)
    user = User.objects.get(username=username)
    # print(user)
    group = Group.objects.get(id=groupID)
    print("this is my group")
    group.user_set.add(user)
    # print(group)
    return HttpResponse(json.dumps({"g_id": groupID}), status=200, content_type="application/json")

# @login_required
# @csrf_exempt
# def createGroups(request):
#     users = User.objects.all()
#     print("yes")
#     print(users)
#     username_id = request.user
#     if request.method == 'POST':
#         form = GroupingForm(request.POST)
#         selected = request.POST.getlist('selected_user[]')
#         if form.is_valid():
#             group = Group.objects.create(
#                 name=form.cleaned_data['name'],
#             )
#             group.save()
#             for user_selected in selected:
#                 print(type (user_selected))
#                 user = User.objects.get(username=user_selected)
#                 print(type (user))
#                 group.user_set.add(user)
#                 group.save()
#
#
#
#     else:
#         form = GroupingForm()
#     variables = RequestContext(request, {
#         'form':form, 'users':users
#     })
#     return render_to_response(
#         'groupmanagement/createGroups.html',
#         variables,
#     )
#
#     group.save()
#     return HttpResponse(json.dumps({"g_id" : groupID}), status=200, content_type="application/json")


@csrf_exempt
def removeMember(request):
    username = request.POST.get('username')
    groupID = request.POST.get('groupID')
    user = User.objects.get(username=username)
    group = Group.objects.get(id=groupID)
    group.user_set.remove(user)
    return HttpResponse(json.dumps({"g_id": groupID}), status=200, content_type="application/json")


@csrf_exempt
def addReports(request):
    user = request.user
    reports = report.objects.all().filter(username_id=user)
    if request.POST.get('hid'):
        g_id = request.POST.get('id')
    if request.POST.get('selected_report'):
        g_id = Group.objects.get(id=request.POST.get('id'))
        addedReport = report.objects.get(title=request.POST.get('selected_report'))
        groupR = GroupReports.objects.create(group=g_id, report_document=addedReport)

    return render(request, 'groupmanagement/addReports.html',
                              {'reports': reports, 'user': user, 'g_id': g_id})


@csrf_exempt
@login_required()
def groupHome(request):
    user = request.user
    print(user)
    return render_to_response('groupmanagement/groupHome.html', {"user", user})
