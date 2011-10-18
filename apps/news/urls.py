from django.conf.urls.defaults import *
from views import subscribe, unsubscribe, user, delete_user

urlpatterns = patterns('',
    url('^subscribe/$', subscribe),
    url('^unsubscribe/(.*)/$', unsubscribe),
    url('^user/(.*)/$', user),
    url('^delete/(.*)/$', delete_user)
)