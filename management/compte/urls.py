from django.urls import path

from django.contrib.auth import views
from compte import views as views_fun

app_name = "compte"

urlpatterns = [
    path('', views_fun.login_view, name='login_view'),
    #path('pageaccueil/', views.pageAccueil, name='pageaccueil'),
    path('register/', views_fun.register_view, name='register_view'),
    path('adminpage/', views_fun.admin_view, name='adminpage'),
    path('teacher/', views_fun.teacher_view, name='teacherpage'),
    path('student/', views_fun.student_view, name='studentpage'),
    path('logout', views_fun.lougout_view, name="lougout_view"),
   
    path('admin_register_user/', views_fun.register_admin_user, name="admin_register_user"),
    path('admin_update_user/<int:pk>/', views_fun.AdminUpdateUser, name="admin_update_user"),
    path('admin_delete_user/<int:pk>/', views_fun.AdminDeleteUser, name="admin_delete_user"),
    #path('home/', home, name='home'),
    #path('logout/', deconnexion, name='logout'),
    #path('profile/', profile, name="profile"),



    path('reset_password', views.PasswordResetView.as_view(), name= "reset_password"),
    path('password_reset_sent', views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]