from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .form_user import SignUpForm, LoginForm
# Create your views here.

def register_view(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Votre compte utilisateur est crée avec succée')
            return redirect('login_view')
        else:
             messages.success(request, 'Formulaire invalide')
    else:
        form = SignUpForm()
    return render(request,'register.html', {'form': form, 'msg': msg})




def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_admin:
                login(request, user)
                return redirect('adminpage')
            elif user is not None and user.is_teacher:
                login(request, user)
                return redirect('teacherpage')
            elif user is not None and user.is_student:
                login(request, user)
                return redirect('studentpage')
            else:
                messages.success(request, 'Mauvaise authentification')
        else:
            messages.success(request, 'Formulaire invalide')
    return render(request, 'login.html', {'form': form})

def lougout_view(request):
    logout(request)
    return redirect('login_view')

def admin_view(request):
    return render(request,'admin.html')


def teacher_view(request):
    return render(request,'teacher.html')


def student_view(request):
    return render(request,'student.html')