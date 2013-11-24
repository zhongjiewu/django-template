from django.conf.urls import patterns, include, url
from django.contrib import admin

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'raas.views.landing', name='landing'),
    url(r'^domain/new/$', 'raas.views.new_domain', name='new_domain'),
    url(r'^domain/upload/$', 'raas.views.upload_file', name='upload_file'),

    # domains
    url(r'^domains/$', 'raas.views.domains.index'),
    url(r'^domains/(?P<id>[^/]*)', 'raas.views.domains.edit'),

    # API
    url(r'^api/setup_domain', 'raas.apis.setup_domain'),
    url(r'^api/upload_file', 'raas.apis.upload_data'),


    # admin views
    url(r'^admin/', include(admin.site.urls)),

    # user login, logout, registration views
    (r'^accounts/', include('registration.backends.default.urls')),

    url(r'^users/sign_out', 'django.contrib.auth.views.logout',
        {'next_page': '/'},
        name="destroy_user_session"),
    url(r'^users/sign_in', 'django.contrib.auth.views.login',
        {'template_name': 'auth/user_signin.html'},
        name="new_user_session"),
    url(r'^users/reset_password_done$', 'django.contrib.auth.views.password_reset_done',
        {'template_name': 'auth/reset_passwd_done.html'},
        name="reset_password_done"),
    url(r'^users/reset_password$', 'django.contrib.auth.views.password_reset',
        {'template_name': 'auth/reset_passwd.html',
         'from_email': '2cloudthinkers@gmail.com'},
        name="reset_password"),
    url(r'^reset/(?P<uidb36>[0-9A-Za-z]{1,13})/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm',
         {'template_name': 'auth/reset_passwd_confirm.html'},
        name="reset_password_confirm"),
    url(r'^reset/done$', 'django.contrib.auth.views.password_reset_complete',
        {'template_name': 'auth/reset_passwd_complete.html'},
        name="reset_password_complete"),

    # work flow
    url(r'^start$', 'raas.views.raas_start', name='raas_start'),
    url(r'^jobs$', 'raas.views.raas_job', name='raas_job'),

    # demo links
    url(r'^demo/product/(?P<pid>[^/]*)', 'raas.views.demo_view'),
    url(r'^demo/api/similar_items', 'raas.apis.similar_items_demo'),
    # js library for demo
    url(r'user-js/src/raas.js', 'raas.views.raas_js'),
)