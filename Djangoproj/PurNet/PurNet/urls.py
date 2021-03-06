from django.conf.urls import patterns, include, url
from django.contrib.auth import views as auth_views
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'PurNet.views.index'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
                       url(r'^user/password/reset/$', 'django.contrib.auth.views.password_reset', {'post_reset_redirect' : '/user/password/reset/done/', 'template_name': 'login/password_reset_form.html'},name="password_reset"),
    url(r'^user/password/reset/done/$','django.contrib.auth.views.password_reset_done', {'template_name': 'login/password_reset_form_done.html'}),
                       url(r'^user/password/reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm', {'post_reset_redirect' : '/user/password/done/', 'template_name': 'login/password_reset_confirm.html'}, name="password_reset_confirm"),
    url(r'^user/password/done/$', 'django.contrib.auth.views.password_reset_complete', {'template_name': "login/password_reset_complete.html"}),
    url(r'^change/password/$','reset.views.change_password', name='changepassword'),
    #url(r'^mang_acct/', include('mang_acct.urls')),
    #url(r'^course_mang/', include('course_mang.urls')),
    #url(r'^create_acct/', include('create_acct.urls')),
    url(r'^login/', include('login.urls')),
    url(r'^inbox/', include('inbox.urls')),
    #url(r'^pass_mang/', include('pass_mang.urls')),
    #url(r'^qa_forums/', include('qa_forums.urls')),
    #url(r'^rate_prof/', include('rate_prof.urls')),
    #url(r'^reset/', include('reset.urls')),
    url(r'^user_homepage/', include('user_homepage.urls')),
    #url(r'^admin/', include(admin.site.urls)),
)
