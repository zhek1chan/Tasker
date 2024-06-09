
from django.contrib import admin
from django.urls import path
from todo import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    #Auth
    path('signupuser', views.signupuser, name='signupuser'),
    path('logoutuser', views.logoutuser, name='logoutuser'),
    path('loginuser', views.loginuser, name='loginuser'),

    #todos
    path('current', views.currenttodos, name='currenttodos'),
    path('completed', views.completedtodos, name='completedtodos'),
    path('', views.home, name='home'),
    path('create', views.createtodo, name='createtodo'),
    path('todo/<int:todo_pk>', views.viewtodo, name='viewtodo'),
    path('todo/<int:todo_pk>/complete', views.completetodo, name='completetodo'),
    path('todo/<int:todo_pk>/delete', views.deletetodo, name='deletetodo'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
