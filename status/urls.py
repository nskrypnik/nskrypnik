from django.conf.urls.defaults import *

urlpatterns = patterns('',
        (r'^change/$', 'status.views.change'),
)

