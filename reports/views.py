from django.shortcuts import render
from .forms import *
from reports.models import *
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.core.files.storage import FileSystemStorage

# Create your views here.
@csrf_exempt
def createReport(request):
    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            report_object = report.objects.create(
                title=form.cleaned_data['title'],
                timestamp=form.cleaned_data['timestamp'],
                short_description=form.cleaned_data['short_description'],
                detailed_description=form.cleaned_data['detailed_description'],
                status_state=form.cleaned_data['status_state'],
                location=form.cleaned_data['location'],
                is_encrypted = form.cleaned_data['is_encrypted']

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