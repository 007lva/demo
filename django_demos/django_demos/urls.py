from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'jqgrid_demo.views.init', name='init'),
    url(r'^crud', 'jqgrid_demo.views.crud', name='crud'),
    url(r'^search', 'jqgrid_demo.views.search', name='search'),
    url(r'^load', 'jqgrid_demo.views.load', name='load'),
    #url(r'^ajax2', 'jqgrid_demo.views.ajax2', name='ajax2'),
    # url(r'^$', 'django_demos.views.home', name='home'),
    # url(r'^django_demos/', include('django_demos.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
