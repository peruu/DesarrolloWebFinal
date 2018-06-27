from django.urls import path
from book import views

urlpatterns = [
    #CRUD BOOKUSER
	path('index/', views.index, name="index"),
	path('list_book', views.list_book, name="list_book"),
    path('add_book/', views.add_book, name="add_book"),
    path('edit_book/<str:id>', views.edit_book, name="edit_book"),
    path('detail_book/<str:id>', views.detail_book, name="detail_book"),
    path('view_book/<str:id>', views.view_book, name="view_book"),
	path('delete_book/<str:id>', views.delete_book, name="delete_book"),
	path('view_sales/', views.view_sales, name='view_sales'),
	path('view_both/', views.view_both, name='view_both'),
]
