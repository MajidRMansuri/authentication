# from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_view
from .form import Loginform,PasswordChange,ForgetPassword,ResetPassword

urlpatterns = [
    # path('admin/', admin.site.urls),
    path("index",views.index,name='index'),
    path('',views.Registration.as_view()),
    path("account/login/", auth_view.LoginView.as_view(template_name='login.html',authentication_form=Loginform),name="login"),
    path('Profile/',views.Profile_edit.as_view(),name='Profile'),
    path('PasswordChange/',auth_view.PasswordChangeView.as_view(template_name='changepassword.html',form_class=PasswordChange,success_url="/changepassworddone/"),name="PasswordChange"),
    path("changepassworddone/",auth_view.PasswordChangeDoneView.as_view(template_name="passworddone.html"),name="changepassworddone"),
    

    path('password-reset/',auth_view.PasswordResetView.as_view(template_name='passwordchangeEmail.html',form_class=ForgetPassword),name='password_reset'),
    path('password-reset/done/',auth_view.PasswordResetDoneView.as_view(template_name="sentemail.html"),name="password_reset_done"),
    path('password-reset-confirm/<uidb64>/<token>/',auth_view.PasswordResetConfirmView.as_view(template_name="PasswordResetConfirm.html",form_class=ResetPassword),name='password_reset_confirm'),
    path("password-reset-complete",auth_view.PasswordResetCompleteView.as_view(template_name='PasswordResetCompleted.html'),name="password_reset_complete")
]
