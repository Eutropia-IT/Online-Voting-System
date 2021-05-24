"""OnlineVotingSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from user import views as user_views
from home import views as home_views
from election import views as elec_views
from vote import views as vote_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
#     path('',home_views.homepage, name='home'),
    path('',user_views.dashboard,name='dashboard'),
    path('edit-info/',user_views.edit_info,name='edit-info'),
    path('register/',user_views.register,name='register'),
    path('result/',vote_views.result,name='result'),#need to add election name to url path
    path('elections/<str:elecName>',elec_views.election,name='elections'),
    path('election-worker/',elec_views.electionWorker,name='election-worker'),
    path('arcives/',elec_views.aricves,name='arcives'),
    path('arcives/<str:elecName>',elec_views.publicResult,name='publicRUS'),
    path('vote/',vote_views.vote,name='vote'),
    path('login/',auth_views.LoginView.as_view(redirect_authenticated_user=True, template_name='home/home.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='home/logout.html'),name='logout'),

    path('password-change/',
         auth_views.PasswordChangeView.as_view(template_name='user/password_change.html'),
         name='password_change'),
    path('password-change/done/',
         auth_views.PasswordChangeDoneView.as_view(template_name='user/password_change_done.html'),
         name='password_change_done'),
         
    path('password-reset/',
         auth_views.PasswordResetView.as_view(template_name='home/password_reset.html'),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='home/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='home/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='home/password_reset_complete.html'),
         name='password_reset_complete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)