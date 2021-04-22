<<<<<<< HEAD
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegister, ProfileUpdate, UserUpdate

def register(request):

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f"Created Successfully")
            return redirect('login')
    else:
        form = UserRegister()
    context = {
        'form':form
    }
    return render(request,"register.html", context)

@login_required
def profile(request):

    title = 'Profile'
    if request.method == "POST":
        u_form = UserUpdate(request.POST, instance=request.user)
        p_form = ProfileUpdate(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f"Profile Successfully Updated !")
            return redirect('profile')
    else:
        u_form = UserUpdate(instance=request.user)
        p_form = ProfileUpdate(instance=request.user.profile)
    context = {
        'title':title,
        'u_form':u_form,
        'p_form':p_form 
    }
    return render(request,'profile.html', context)




def login(request):

    context = {
        'title':title,
        'form':form
    }
    return render(request,'./teziapp/login.html', context)


def logout(request):

    context = {
        'title':title,
        'form':form
    }
    return render(request,'./teziapp/logout.html', context)
=======
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import permissions
from .models import *
from rest_framework import status
from .permissions import IsAdminOrReadOnly
from rest_framework.decorators import action, permission_classes as permission_decorator
from rest_framework.permissions import AllowAny
from django.contrib.auth import login

# Create your views here.
class IsAssigned(permissions.BasePermission): 
    """
    Only person who assigned has permission
    """
    def has_object_permission(self, request, view, obj):
		# check if user who launched request is object owner 
        if obj.assigned_to == request.user: 
            return True
        return False
class IsReadOnlyOrIsAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        authenticated = request.user.is_authenticated
        if not authenticated:
            if view.action == '/':
                return True
            else:
                return False
        else:
            return True
>>>>>>> 9d9c1824772b8166a10bfe6542bb4b4d795420e2
