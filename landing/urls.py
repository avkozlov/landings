from django.conf.urls import patterns, include, url
from django.contrib import admin
from land.views import home
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'land.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),







) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)