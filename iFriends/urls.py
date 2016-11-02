from django.conf.urls import patterns, include, url
from django.contrib import admin

details1 = {'opts':('name','email')}


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'iFriends.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^People/$', 'Person.views.index'),
    url(r'^People/Info/(?P<pID>\d+)/$', 'Person.views.details', details1, name='details'),
    url(r'^People/vindex/$', 'Person.views.view_index'),
    url(r'^People/calendar/$', 'Person.views.view_calendar'),
    url(r'^People/contact/$', 'Person.views.contact_view'),
    url(r'^People/Form/(?P<pID>\d+)/$', 'Person.views.person_form'),
    url(r'^People/posts/$', 'Person.views.post_list', name='post_list'),
    url(r'^People/post/(?P<pk>\d+)/$', 'Person.views.post_detail', name='post_detail'),
    url(r'^People/post/new/$', 'Person.views.post_new', name='post_new'),
    url(r'^People/post/(?P<pk>\d+)/edit/$', 'Person.views.post_edit', name='post_edit'),
    url(r'^admin/', include(admin.site.urls)),
)
