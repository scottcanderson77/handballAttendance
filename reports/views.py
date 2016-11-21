from django.shortcuts import render
from .forms import *
from reports.models import *
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User


# Create your views here.
@csrf_exempt
def createReport(request):
    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=True)
            report_object = report.objects.create(
                title=form.cleaned_data['title'],
                timestamp=form.cleaned_data['timestamp'],
                short_description=form.cleaned_data['short_description'],
                detailed_description=form.cleaned_data['detailed_description'],
                status_state=form.cleaned_data['status_state'],
                location=form.cleaned_data['location'],
                is_encrypted = form.cleaned_data['is_encrypted'],
                username_id= request.user

            )
    else:
        form = ReportForm()
    variables = RequestContext(request, {
        'form': form
    })


    return render_to_response(
        'reports/createReports.html',
        variables,
    )

def viewReports(request):
    user = request.user
    reports = report.objects.all().filter(is_public="True")
    return render(request, 'reports/viewReports.html', {})

def viewYourReports(request):
    user = request.user
    reports = report.objects.all().filter(username_id=user)
    return render(request, 'reports/viewYourReports.html', {})

def searchReport(request, field):
    reports.report.objects.all().filter()

def editReport(request, report_id):
    report = report.object.filter(report_id=report_id)
    if request.POST:
        form = ReportForm(request.POST, instance=report)
        if form.is_valid():
            form.save()
            return redirect('Reports')
        else:
            form.ReportForm(instance=report)
            template = 'editReport.html'
            report = { 'form' : form}
            return render_to_response(template, report, RequestContext(request))

def deleteReport(request, report_id):
    report.object.filter(report_id=report_id).delete()
