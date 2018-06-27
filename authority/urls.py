from django.urls import path
from authority import views
urlpatterns = [
	path('register/',views.signup_user,name="signup_user"),
    path('',views.login_user,name="login_user"),
    path('logout/',views.logout_user,name="logout_user"),
    path('list_users/',views.list_users,name="list_users"),
    #path('create_admin/',views.signup_admin,name="create_admin")

    # path('edit_user/<str:user_run>',views.edit_user,name='user_edit'),
    path('remove_user/<str:user_run>',views.remove_user,name='user_remove'),


]
