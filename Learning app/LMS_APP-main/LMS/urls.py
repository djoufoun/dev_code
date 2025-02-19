from django.contrib import admin
from django.urls import include, path
from .import views
from . import user_login
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base', views.BASE, name='base'),
    path('404', views.PAGE_NOT_FOUND, name='404'),
    path('', views.HOME, name='home'),
    path('singlecourse', views.SINGLECOURSE, name='singlecourse'),
    path('course/filter-data',views.filter_data,name="filter-data"),
    path('search',views.SEARCH_COURSE,name='search_course'),
    path('course/<slug:slug>', views.COURSE_DETAIL, name='course_detail'),
    path('aboutus', views.ABOUTUS, name='aboutus'),
    path('contactus', views.CONTACTUS, name='contactus'),

    path('accounts/register', user_login.REGISTER, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('doLogin', user_login.DOLOGIN, name='doLogin'),
    path('accounts/profile', user_login.PROFILE, name='profile'),
    path('accounts/profile/update', user_login.PROFILE_UPDATE, name='profile_update'),

    path('checkout/<slug:slug>', views.CHECKOUT, name='checkout'),
    path('my_course', views.MY_COURSE, name='my_course'),
    path('course/watch/<slug:slug>', views.WATCH_COURSE, name='watch_course'),

    path('verify_payment', views.VERIFY_PAYMENT, name='verify_payment'),




    

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
