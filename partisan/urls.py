# partisan.urls
# Application url definition and routers.
#
# Author:   Benjamin Bengfort <bbengfort@districtdatalabs.com>
# Created:  Sun Jul 17 18:33:45 2016 -0400
#
# Copyright (C) 2015 District Data Labs
# For license information, see LICENSE.txt
#
# ID: urls.py [5277a6e] benjamin@bengfort.com $

"""
Partisan Discourse URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/

Examples:

Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')

Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')

Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

##########################################################################
## Imports
##########################################################################

from django.contrib import admin
from rest_framework import routers
from django.conf.urls import include, url

from partisan.views import *
from members.views import *
from corpus.views import *

##########################################################################
## Endpoint Discovery
##########################################################################

## API
router = routers.DefaultRouter()
router.register(r'status', HeartbeatViewSet, "status")
router.register(r'users', UserViewSet)
router.register(r'documents', DocumentViewSet)

##########################################################################
## URL Patterns
##########################################################################

urlpatterns = [
    # Admin URLs
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # Application URLs
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^terms/$', TemplateView.as_view(template_name='site/legal/terms.html'), name='terms'),
    url(r'^privacy/$', TemplateView.as_view(template_name='site/legal/privacy.html'), name='privacy'),

    # Authentication URLs
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('^accounts/', include('django.contrib.auth.urls')),

    ## REST API Urls
    url(r'^api/', include(router.urls, namespace="api")),

    # Member, and Organization URLs
    # !important: must be last and ordered specifically
    url('', include('corpus.urls', namespace='corpus')),
    url('', include('members.urls', namespace='member')),
]
