from django.conf.urls import include, url
from django.contrib.auth.views import login
from registration.views import *
from groupmanagement.views import *
from reports.views import *
from message.views import *
from practice.views import *
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
         url(r'^$', login),
         url(r'^logout/$', logout_page),
         url(r'^accounts/login/$', login),
         url(r'^register/$', register),
         url(r'^register/success/$', register_success),
         url(r'^home/$', home),
         url(r'^createGroup/$', createGroup),
         url(r'^admin/', admin.site.urls),
         url(r'^allusers/(.*)', displayUsers),
         url(r'^YourGroups/', viewGroups),
         url(r'^group/(.*)', groupActionsView),
         url(r'^addmember/', addMember),
         url(r'^addReports/$', addReports),
         url(r'^removeMember', removeMember),
         url(r'^createReport/$', createReport),
         url(r'^editReport/$', editReport),
         url(r'^viewYourReport/$', viewYourReports),
         url(r'^viewReportDescription/$', viewReports),
         url(r'^suspendUsers', suspendUsers),
         url(r'^reinstateUsers', reinstateUsers),
         url(r'^UpdateSuspension', UpdateSuspension),
         url(r'^viewReport/$', viewReport),
         url(r'^searchReport/$', searchReports),
         url(r'^deleteReport/$', deleteReport),
         url(r'^createFolder/$', createFolder),
         url(r'^renameFolder/$', renameFolder),
         url(r'^deleteFolder/$', deleteFolder),
         url(r'^addToFolder/$', addToFolder),
         url(r'^viewFolderContent/$', viewFolderContent),
         url(r'^removeReportFromFolder', removeReports),
         url(r'^viewFolder/$', viewFolder),
         url(r'^viewFolderDescription/$', viewFolderDescription),
         url(r'^messageHome/$', messageHome),
         url(r'^allMessages/$', displayMessage),
         url(r'^checkMessage/$', checkMessage),
         url(r'^createMessage/$', createMessage),
         url(r'^changeUserRoles/', changeUserRole),
         url(r'^updatePrivilege/', updatePrivilege),
         url(r'^allMessages/(?P<message_id>[0-9]+)/$', detail, name="detail"),
         url(r'^checkMessage/(?P<message_id>[0-9]+)/$', detail, name="detail"),
         url(r'^deleteMessage/(?P<message_id>[0-9]+)/$', deleteMessage, name="delete"),
         url(r'^download/(?P<file_name>.*.+)$', download),
         url(r'^reportHome/$', reportHome, name="report"),
         url(r'^folderHome/$', folderHome, name="folder"),
         url(r'^groupHome/$', groupHome, name="group"),
         url(r'^practiceHome/$', practiceHome),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
