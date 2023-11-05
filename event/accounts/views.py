from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth import authenticate , login, logout

from django.urls import reverse

from  accounts.models import ProfileModel
from accounts.forms import ProfileEditForm , UserEditForm ,ProfileRegisterForm

import ticketing
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

#=================================1

# def loginView(request):

#     return HttpResponse('<h1 style="color:white ;background-color:gray;padding:20px; text-align:center">Login</h1>')

#=================================2

# def loginView(request):

#      return render(request,'accounts/login.html',{})

#=================================3
 
# def loginView(request):
#     if request.method=="POST":
#             username=request.POST.get("username")
#             password=request.POST.get("password")
#             user=authenticate(request, username=username , password=password)

#             if user is not None:
#                   pass
#             else:
#                   pass


     

#     return render(request,'accounts/login.html',{})

#=================================4
 
def loginView(request):
    #POST
    if request.method=="POST":
            username=request.POST.get("username")
            password=request.POST.get("password")
            user=authenticate(request, username=username , password=password)

            if user is not None:
                  login(request,user)
                  if  request.GET.get('next'):
                        return HttpResponseRedirect(request.GET.get('next'))
                  
                  return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
                  
                  


                  # return HttpResponseRedirect(reverse("time-list"))
            else:
                  context={
                        "username":username ,
                        "errorMessage":"Not Found"

                  }
                  return render(request,'accounts/login.html',context)


     
   #get
    return render(request,'accounts/login.html',{})

 #================
def logoutView(request):
      logout(request)
      return HttpResponseRedirect(reverse("ticketing:event-list"))

#=====================
 
@login_required
def profileView(request):
      profile = request.user.profile
      dataJoin=request.user.date_joined.strftime("%B  %d, %Y ")
      context={

            "profile":profile ,
            "dataJoin" :dataJoin

      }
      return render(request ,"accounts/profile.html",context)


#==============================================
def profileregisterView(request):
      if request.method=="POST":
            profileRegisterForm=ProfileRegisterForm(request.POST ,request.FILES)
            if profileRegisterForm.is_valid():
                  user = User.objects.create_user(username=profileRegisterForm.cleaned_data["username"],
                                                 email=profileRegisterForm.cleaned_data["email"],                                                 
                                                 password=profileRegisterForm.cleaned_data["password"],
                                                 first_name=profileRegisterForm.cleaned_data["first_name"],
                                                 last_name=profileRegisterForm.cleaned_data["last_name"]
                                                 

                  )
                  
                  user.save()
                  profileModel =ProfileModel(user=user ,
                                             profileImage=profileRegisterForm.cleaned_data["profileImage"] ,
                                             gender=profileRegisterForm.cleaned_data["gender"] ,
                                             credit=profileRegisterForm.cleaned_data["credit"] 

                                             

                        
                  )
                  profileModel.save()
                  return HttpResponseRedirect(reverse("accounts:login"))


            
      else:
            profileRegisterForm=ProfileRegisterForm()
           
      context={
            "formData":profileRegisterForm 
            

      }
      return render(request ,"accounts/profile-register.html",context)


#=======================================
def profileEditView(request):
      if request.method == "POST":
           profileEditForm= ProfileEditForm(request.POST,request.FILES,instance=request.user.profile)
           userEditForm=UserEditForm(request.POST,instance=request.user)
           if profileEditForm.is_valid and  userEditForm.is_valid  :
                 profileEditForm.save()
                 userEditForm.save()
                 return HttpResponseRedirect(reverse("accounts:profile"))

                 


      else:
           profileEditForm= ProfileEditForm(instance=request.user.profile)
           userEditForm=UserEditForm(instance=request.user)

      context={
            
            "profileEditForm":profileEditForm ,
            "profileImage":request.user.profile.profileImage,
            "userEditForm" :userEditForm

      }

      return  render (request, "accounts/profile-edit.html" , context)




  

             

      