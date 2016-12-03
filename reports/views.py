from django.shortcuts import render
from .forms import *
from reports.models import *
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.utils import timezone


# Create your views here.
@csrf_exempt
def createReport(request):
    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            newsubmit = form.save(commit=False)
            newsubmit.user

            # checked = False
            # encrypted = False
            # if request.POST.get("is_private", False):
            #     checked = True
            #     encrypted = True
            # if request.POST.get("is_encrypted", False):
            #     encrypted = True
            #
            # report_object = report.objects.create(
            #     title=form.cleaned_data['title'],
            #     timestamp=timezone.now(),
            #     short_description=form.cleaned_data['short_description'],
            #     detailed_description=form.cleaned_data['detailed_description'],
            #     is_private = checked,
            #     location=form.cleaned_data['location'],
            #     is_encrypted = encrypted,
            #     username_id= request.user
            #
            # )
            # report_object.save()

    else:
        form = ReportForm()
    variables = RequestContext(request, {
        'form': form
    })


    return render_to_response(
        'reports/createReports.html',
        variables,
    )



@csrf_exempt
def createFolder(request):
    reports = report.objects.all()
    username_id = request.user
    if request.method == 'POST':
        form = FolderForm(request.POST, request.FILES)
        selected = request.POST.getlist('selected_report[]')
        if form.is_valid():
            folder_object = folder.objects.create(
                title=form.cleaned_data['title'], username_id=username_id
            )
            for report_selected in selected:
                re = report.objects.get(title=report_selected)
                folder_object.added_reports.add(re)

    else:
        form = FolderForm()
    variables = RequestContext(request, {
        'form': form, 'reports':reports
    })

    return render_to_response(
        'reports/createFolder.html',
        variables,
    )
def renameFolder(request):
    folders = folder.objects.all()
    selected = request.POST.getlist('selected_folder[]')
    if request.method == 'POST':
        form = FolderForm(request.POST)
        if form.is_valid():
            title=form.cleaned_data['title']

            for folder_selected in selected:
                print(folder_selected)
                fs = folder.objects.get(title=folder_selected)
                fs.title = title
                fs.save()
    else:
        form = FolderForm()
    variables = RequestContext(request, {
        'form': form, 'folders':folders
    })

    return render_to_response(
        'reports/renameFolder.html',
        variables,
    )

def deleteFolder(request):
    folders = folder.objects.all()
    selected = request.POST.getlist('selected_folder[]')
    if request.method == 'POST':
        for folder_selected in selected:
            fs = folder.objects.get(title=folder_selected)
            fs.delete()
    else:
        pass
    variables = RequestContext(request, {
        'folders': folders
    })

    return render_to_response(
        'reports/deleteFolder.html',
        variables,
    )



def viewFolder(request):
    user = request.user
    folders = folder.objects.all()
    reports = folder.objects.all()
    return render(request, 'reports/viewFolders.html', {'folders': folders, 'reports':reports, 'user': user})

def viewReports(request):
    user = request.user
    reports = report.objects.all().filter(is_private="False")
    folders = folder.objects.all()
    return render(request, 'reports/viewReports.html', {'user': user, 'reports': reports, 'folders':folders})

def viewReport(request):
    user = request.user
    title = request.POST.get("selected_report")
    #title = request.POST.getlist("selected_report[]")
    #for report_selected in title:
     #   rs = report.objects.get(title=report_selected)

    print(title)
    rs = report.objects.get(title=title)
    return render(request, 'reports/viewReportDescription.html', {'rs': rs, 'user':user})



def viewYourReports(request):
    user = request.user
    reports = report.objects.all().filter(username_id=user)
    folders = folder.objects.all().filter(username_id=user)
    return render(request, 'reports/viewYourReports.html', {'reports':reports, 'user': user, 'folders':folders })

def searchReport(request, field):
    reports.report.objects.all().filter()

def editReport(request):
    user = request.user
    title = request.POST.get("title")
    short = request.POST.get("short")
    detailed = request.POST.get("detailed")
    is_private = request.POST.get("private")
    original = request.POST.get("original")
    if(request.POST.getlist('updated')):
        reports = report.objects.get(title=original)
        reports.title = title
        reports.short_description = short
        reports.detailed_description = detailed
        if is_private == "private":
            reports.is_private = True
        else:
            reports.is_private = False

        #reports.is_private = is_private
        reports.save()

    return render(request, 'reports/editReport.html', {'user': user, 'title': title, 'short': short, 'detailed':detailed, 'private': is_private})



def deleteReport(request):
    user = request.user
    id = request.POST.get("id")
    report.objects.filter(id=id).delete()
    return render(request, 'reports/viewYourReports.html', {'user':user})


def searchReport(request):
    query_string = request.GET['q']
    results = report.objects.annotate(
        search=SearchVector('title', 'short_description', 'detailed_description'),
    ).filter(search=query_string).order_by('timestamp')
    return render_to_response('reports/searchReports.html', {'results': results }, context_instance=RequestContext(request))
