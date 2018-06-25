from django.urls import path
from book import views
<<<<<<< HEAD
urlpatterns = [
    
	# path('inicio/', views.inicio, name="inicio"),
	# path('list_book', views.list_book, name="list_book"),
    path('add_book/', views.add_book, name="add_book"),
<<<<<<< HEAD
	# path('update_book/<str:id>', views.update_book, name="update_book"),
	# path('delete_book/<str:id>', views.delete_book, name="delete_book"),

=======
	path('update_book/<str:id>', views.update_book, name="update_book"),
	path('delete_book/<str:id>', views.delete_book, name="delete_book"),
>>>>>>> pr/4
	#HAY QUE HACER FUNCIONAR EL BOTÓN DE AGREGAR LIBRO EN LIST_BOOK
=======


urlpatterns = [
    path('',views.index,name="index"),
    path('/genres',views.add_genres,name="genres"),
>>>>>>> fd0270f1a5aecbefe957dd25fc20d77e6031b0f0
]
