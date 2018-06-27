from django.forms import ModelForm
from book.models import *


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = [
            'title',
            'author', 
            'editorial', 
            'book_type', 
            'genre', 
            'language', 
            'original', 
            'transaction', 
            'price', 
            'comment', 
            'number_of_pages', 
            'picture',
        ]

        labels = {
            'title' : 'Título',
            'author' : 'Autor/a', 
            'editorial' : 'Editorial', 
            'book_type' : 'Tipo de texto', 
            'genre' : 'Género', 
            'language' : 'Idioma', 
            'original' : 'Original o no', 
            'transaction' : 'Tipo de transacción', 
            'price' : 'Valor', 
            'comment' : 'Comentario', 
            'number_of_pages' : 'Número de páginas', 
            'picture' : 'Imagen del texto', 
        }


