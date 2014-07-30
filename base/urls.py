from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'Site.views.home', name='home'),
    url(r'^cadastrar/usuario/$', 'User.views.userCreate', name='user-create'),
    url(r'^alterar/usuario/(\d+)$', 'User.views.userUpdate', name='user-update'),
    url(r'^listar/usuario/$', 'User.views.userRead', name='user-read'),
    url(r'^visualizar/usuario/(\w+<id>)$', 'User.views.userView', name='user-view'),

    # Examples:
    # url(r'^$', 'base.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
