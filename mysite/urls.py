"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
from core.urls import urlpatterns as core_urls
from user.urls import urlpatterns as user_urls
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from core.api.urls import urlpatterns as core_api_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(core_urls)),
    path('user/', include(user_urls)),
    path('i18n/',include('django.conf.urls.i18n')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(core_api_urls)),
    
    
 

]

urlpatterns += i18n_patterns(
     path('', include(core_urls)),
     path('rosetta/', include('rosetta.urls')),
                             )

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        path('rosetta/', include('rosetta.urls')),
    ]


