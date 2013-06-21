from django.conf.urls.defaults import url
from django.conf.urls.defaults import include
from django.conf.urls.defaults import patterns
from django.conf.urls.defaults import *
from registration.views import register

from gstudio.forms import RecaptchaRegistrationForm

urlpatterns = patterns(
    '',
    (r'^raw/(?P<name>.+)/', 'mobwrite.views.raw'),
    (r'^r/(?P<name>.+)/', 'mobwrite.views.raw'),
    (r'^m/(?P<name>.+)/', 'mobwrite.views.html'),
    #(r'^t/(?P<name>.+)/', 'mobwrite.views.text'),
    #(r'^$', 'app.views.index'),
    #(r'^new/$', 'mobwrite.views.new'),
    (r'^mobwrite/', 'mobwrite.views.mobwrite'), 
    #(r'^test/', test_view), 
    #(r'^synclink/$','mobwrite.views.syncfx'),
    (r'^deleteLink/$','textbapp.views.deleteFx'),

)