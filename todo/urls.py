
from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.login_view,name = "login"),
    path('signup/',views.signup,name = 'signup'),
    path('todo/',views.todo_page,name = 'todo'),
    path('todo/delete/<int:id>/',views.delete_task,name='delete'),
    path('logout/',views.logout_view,name = 'logout'),
]
