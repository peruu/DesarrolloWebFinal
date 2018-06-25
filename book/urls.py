from django.urls import path
from book import views

urlpatterns = [
    path('',views.index,name="index"),
	path('inicio/', views.inicio, name="inicio"),
	path('list_book', views.list_book, name="list_book"),
    path('add_book/', views.add_book, name="add_book"),
	path('update_book/<str:id>', views.update_book, name="update_book"),
	path('delete_book/<str:id>', views.delete_book, name="delete_book"),
	#HAY QUE HACER FUNCIONAR EL BOTÓN DE AGREGAR LIBRO EN LIST_BOOK
]