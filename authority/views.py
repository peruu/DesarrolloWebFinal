from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from authority.forms import *
from django.contrib.auth.decorators import login_required
from book.models import *
# from django.contrib.auth.forms import UserCreationForm
#
def login_user(request):
    template_name = "login/login.html"
    data = {}
    logout(request)
    username = password = ""
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            user_profile = UserProfile.objects.get(user= user)
            flag = user_profile.is_user
            if user.is_active:
                if flag:
                    login(request,user)
                    return redirect("inicio")
            else:
                messages.warning(request,"Usuario o contraseña incorrecta")
        else:
            #usuario no existe
            messages.error(request,"Usuario o contraseña incorrecta")
    return render(request,template_name)

def signup_user(request):
    template_name="register/register.html"
    data = {}
    form_admin = SignUpUserForm(request.POST or None)

    if form_admin.is_valid():
        form_admin.save()
        password = form_admin.cleaned_data.get('password1')
        username = form_admin.cleaned_data.get('username')
        user = authenticate(username=username, password=password)
        #CREAR USER PROFILE
        user_profile = UserProfile.objects.create(user=user,is_user=True)
        user_profile.save
        #CREAR USER BOOK
        RUN = form_admin.cleaned_data['RUN']
        commune = form_admin.cleaned_data['commune']
        phone = form_admin.cleaned_data['phone']
        user_book = UserBook.objects.create(user=user_profile,RUN=RUN,commune=commune,phone=phone)
        user_book.save
        messages.success(request, 'Cuenta creada con éxito')
        login(request, user)
        return redirect("index")
    data['form'] = form_admin
    return render(request,template_name,data)
@login_required(login_url="/")
def logout_user(request):
    logout(request)
    return redirect("login_user")

