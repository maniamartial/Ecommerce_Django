"""UmojaWater URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from django import urls
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('products.urls')),
    # path('', include('checkout.urls')),
    path('users/', include('users.urls')),
    path('payments/', include('payments.urls')),

    # Authentication URL patterns

# LogoutView: View for logging out the user
path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),

# PasswordResetView: View for initiating the password reset process
path('password-reset/', auth_views.PasswordResetView.as_view(
     template_name='users/password_reset.html'), name='password_reset'),

# PasswordResetDoneView: View shown after the password reset email has been sent
path('password-reset/done', auth_views.PasswordResetDoneView.as_view(
    template_name='users/password_reset_done.html'), name='password_reset_done'),

# PasswordResetConfirmView: View for confirming the password reset using a unique token
path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
    template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),

# PasswordResetCompleteView: View shown after the password has been successfully reset
path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
    template_name='users/password_reset_complete.html'), name='password_reset_complete'),

]

#setting up to handle the media
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
