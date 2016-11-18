from django.conf.urls import include, url
from django.contrib.auth.views import login
from registration.views import *
from groupmanagement.views import *
from django.contrib import admin

urlpatterns = [
         url(r'^$', login),
         url(r'^logout/$', logout_page),
         url(r'^accounts/login/$', login),
         url(r'^register/$', register),
         url(r'^register/success/$', register_success),
         url(r'^home/$', home),
         url(r'^createGroup/$', createGroup),
         url(r'^admin/', admin.site.urls),
         url(r'^allusers/', displayUsers),
         url(r'^YourGroups/', viewGroups),
         url(r'^group/(.*)', groupActionsView)
]