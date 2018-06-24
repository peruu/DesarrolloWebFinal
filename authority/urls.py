from django.urls import path
from authority import views

urlpatterns = [
    path('',views.login_admin,name="login"),
    path('logout/',views.logout_admin,name="logout"),
    path('create_admin/',views.signup_admin,name="create_admin")

]
