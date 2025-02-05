from django.urls import path
from compte import views

urlpatterns = [
    path('', views.login_view, name='login_view'),
    path('register/', views.register_view, name='register_view'),
    path('adminpage/', views.admin_view, name='adminpage'),
    path('teacher/', views.teacher_view, name='teacherpage'),
    path('student/', views.student_view, name='studentpage'),
    path('logout', views.lougout_view, name="lougout_view")
    #path('home/', home, name='home'),
    #path('logout/', deconnexion, name='logout'),
    #path('profile/', profile, name="profile"),



    #path('reset', views.PasswordResetView.as_view(template_name="password/password_reset.html"), name= "reset_password"),
    #path('reset_done', views.PasswordResetDoneView.as_view(template_name="password/password_reset_sent.html"), name="reset_done"),
    #path('reset/<uidb64>/<token>', views.PasswordResetConfirmView.as_view(template_name="password/password_reset_form.html"), name='reset_confirm'),
    #path('reset_complete', views.PasswordResetCompleteView.as_view(template_name="password/password_reset_done.html"), name='reset_complete'),
]