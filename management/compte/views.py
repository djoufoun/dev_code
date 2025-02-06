from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import *
from students.models import *
# Create your views here.

def register_view(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Votre compte utilisateur est crée avec succée')
            return redirect('compte:login_view')
        else:
             messages.success(request, 'Formulaire invalide')
    else:
        form = SignUpForm()
    return render(request,'comptes/register.html', {'form': form, 'msg': msg})

def views_user(request):
    views_user = User.objects.all()
    
    return render(request, 'compte/views_user.html',{'views_user':views_user})



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
                return render(request, 'roles/accueil.html')
            elif user is not None and user.is_teacher:
                login(request, user)
                return redirect('compte:teacherpage')
            elif user is not None and user.is_student:
                login(request, user)
                return redirect('compte:studentpage')
            else:
                messages.success(request, 'Mauvaise authentification')
        else:
            messages.success(request, 'Formulaire invalide')
    return render(request, 'comptes/login.html', {'form': form})

def lougout_view(request):
    logout(request)
    return redirect('compte:login_view')

def admin_view(request):
    return render(request,'comptes/admin.html')


def teacher_view(request):
    return render(request,'comptes/teacher.html')


def student_view(request):
    liste = Emplois.objects.all()
    note = Note.objects.all()
    views_comment = Comment.objects.all()
    return render(request,'comptes/student.html', {'liste':liste, 'notes':note, 'view_comment':views_comment})







#la Fonction qui permet de enregistrer un utilisateur par l'administrateur
def register_admin_user(request):
   
    if request.method == 'POST':
        form = AdminUserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Votre compte utilisateur est crée avec succée')
            #return redirect('login_view')
        else:
             messages.success(request, 'Formulaire invalide')
    else:
        form = AdminUserRegisterForm()
    views_user = User.objects.all()
    return render(request,'compte/admin_register.html', {'form': form,  'views_user':views_user})

def AdminUpdateUser(request, pk=None):

    if not pk is None:
        data = User.objects.get(id=pk)
        form = AdminUserRegisterForm(instance=data)
        if request.method == "POST":
            form = AdminUserRegisterForm(request.POST, instance=data)
            if form.is_valid():
                form.save()
                messages.success(request, 'La modification est faite avec succès')
                return redirect('compte:admin_register_user') 
            else:
              form = AdminUserRegisterForm()
    context ={'form':form}

    return render(request, 'compte/UpdateUser.html', context)


def AdminDeleteUser(request, pk=None):
    
    if not pk is None:
        query = User.objects.get(id=pk)
        obj = query.username
        if request.POST:
            query.delete()
            messages.success(request, 'La suppression à éffectuée avec succèe!')
            return redirect('compte:admin_register_user')          
    return render(request, 'compte/DeleteUser.html', {'name':obj})