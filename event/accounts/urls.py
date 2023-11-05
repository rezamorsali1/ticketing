from django.urls import path

from accounts import views
 
app_name='accounts'

urlpatterns = [
  
     
    path('login/',views.loginView ,name="login" ) ,
    path('logout/',views.logoutView,name="logout" ) ,
    path('profile/',views.profileView,name="profile" ) ,
    path('profile-register/',views.profileregisterView,name="profile-register" ) ,
    path('profile-edit/',views.profileEditView,name="profile-edit" ) ,






]