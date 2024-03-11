from django.urls import path
from . import views
app_name='user'
urlpatterns=[
    path('login/',views.User_login,name="User_login"),
    path('logout/',views.User_logout,name="User_logout"),
    path('signup/',views.User_register,name="User_register"),
    path('edit/', views.edit_user, name='edit_user'),
]