"""locallibrary URL Configuration

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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.views.generic import RedirectView

from catalog.views import RegisterFormView, UpdateProfile, UserProfile

urlpatterns = [
    path('admin/', admin.site.urls),
]

# Используйте include() чтобы добавлять URL из каталога приложения

urlpatterns += [
    path('catalog/', include('catalog.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', RegisterFormView.as_view(), name="register"),
    path('accounts/update_profile/', UpdateProfile.as_view(), name="update_profile"),
    path('accounts/my_profile/', UserProfile.as_view(), name="profile"),
]

# Добавьте URL соотношения, чтобы перенаправить запросы с корневого URL, на URL приложения
urlpatterns += [
    path('', RedirectView.as_view(url='/catalog/', permanent=True)),
]

# Используйте static() чтобы добавить соотношения для статических файлов
# Только на период разработки
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
