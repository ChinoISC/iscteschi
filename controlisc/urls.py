"""
URL configuration for controlisc project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from api.Home.homeView import Home,Login,LogoutView
from api.Users.user_view import CreateUserView
from api.Activity.view_activity import ActivityView, CreateActivity,CompletedActivity,DeleteActivity,EditActivity
from api.Tables.view_tables import ViewTable
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Home.as_view(),name='index' ),
    path('view_activity',ActivityView.as_view(),name='view_activity' ),
    path('create_user/',CreateUserView.as_view(),name='create_user' ),
    path('create_activity/',CreateActivity.as_view(),name='create_activity' ),
    path('change_completed/',CompletedActivity.as_view(),name='change_completed' ),
    path('change_edit/',EditActivity.as_view(),name='change_edit' ),
    path('change_delete/',DeleteActivity.as_view(),name='change_delete' ),
    path('view_tables_activity/',ViewTable.as_view(),name='view_tables_activity' ),
    path('login/',Login.as_view(),name='login' ),
    path('logout/',LogoutView.as_view(),name='logout' ),
]

urlpatterns += staticfiles_urlpatterns()