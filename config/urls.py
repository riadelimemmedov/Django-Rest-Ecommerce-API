"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from django.utils.translation import gettext_lazy as _

from abstract.constants import AppName

#!Admin Site Configuration
admin.site.site_header = _('Ecommerce Admin')#login page
admin.site.site_title = _('Ecommerce Admin User')#html <title> tag 
admin.site.index_title = _('Welcome My Ecommerce Project')#site administration

urlpatterns = []

if not settings.APP_NAME or settings.APP_NAME not in [app.value for app in AppName]:
    raise Exception(_('Please set app correct name same as abstract.constants.AppName'))


if settings.APP_NAME == AppName.ADMIN.name:
    urlpatterns += [
        path('jet/',include('jet.urls','jet')),
        path("jet/dashboard/", include("jet.dashboard.urls","jet-dashboard")),
        # path("ckeditor/", include("ckeditor_uploader.urls")),
    ]
    
    urlpatterns += i18n_patterns(
        path('admin/',admin.site.urls)
    )
else:
    #App Url
    pass

#!Settings Debug
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
