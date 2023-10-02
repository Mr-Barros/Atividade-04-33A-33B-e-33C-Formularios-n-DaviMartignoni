"""django_project URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from canguru import views

urlpatterns = [
  path("", views.home, name="home"),
  path("users/new/", views.create_user, name="create_user"),
  path("users/reset_password/", 
       auth_views.PasswordResetView.as_view(template_name = "registration/reset_password.html"), 
       name="reset_password"),
  path("users/password_reset/done/", 
       auth_views.PasswordResetDoneView.as_view(template_name = "registration/reset_password_sent.html"), 
       name="password_reset_done"),
  path("users/reset/<uidb64>/<token>/", 
       auth_views.PasswordResetConfirmView.as_view(template_name = "registration/reset_password_form.html"), 
       name="password_reset_confirm"),
  path("users/reset/done/",
       auth_views.PasswordResetCompleteView.as_view(template_name = "registration/reset_password_complete.html"), 
       name="password_reset_complete"),
  path("users/update/<id>", views.update_user),
  path("users/", include("django.contrib.auth.urls")),
  path("comment/add", views.add_comment),
  path("comment/update/<id>", views.update_comment),
  path("comment/delete/<id>", views.delete_comment),
  path("legendary_kangaroo/add", views.add_legendary_kangaroo),
  path("legendary_kangaroo/update/<id>", views.update_legendary_kangaroo),
  path("legendary_kangaroo/delete/<id>", views.delete_legendary_kangaroo),
  path("admin/", admin.site.urls),
]
