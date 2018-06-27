from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	user = models.OneToOneField(User,blank=True, null=True, on_delete=models.CASCADE)
	is_admin = models.BooleanField(default=False)
	is_user = models.BooleanField(default=False)
	def _str_(self):
		return self.user
class UserBook(models.Model):
	user = models.OneToOneField(UserProfile,blank=True, null=True, on_delete=models.CASCADE)
	RUN = models.CharField(max_length=15)
	commune = models.CharField(max_length=20)
	phone = models.CharField(max_length=20)
	def _str_(self):
		return self.user
class Book(models.Model):
	user = models.ForeignKey(UserBook, blank=True, null=True,on_delete=models.CASCADE)
	title = models.CharField(max_length=50)
	author = models.CharField(max_length=30)
	editorial = models.CharField(max_length=30)
	BOOK = 'BOOK'
	BOOK_TYPE_CHOICES = (
		('BOOK', "Libro comun"),
		('COMIC', "Comic"),
		('ESPECIAL_BOOK', "Lectura especializada"),
		('KIDS_BOOK', "Lectura infantil"),
	)
	book_type = models.CharField(
		max_length=20,
		choices=BOOK_TYPE_CHOICES,
		default=BOOK,
	)
	GENRE = 'Género'
	GENRE_CHOICES = (
		('ADVENTURE', "Aventura"),
		('DRAMA', "Drama"),
		('FANTASY', "Fantasía"),
		('FICTION', "Ficción"),
		('ROMANCE', "Romance"),
		('HISTORY', "Historia"),
		('POETRY', "Poesía"),
	)
	genre = models.CharField(
		max_length=20,
		choices=GENRE_CHOICES,
	)
	language = models.CharField(max_length=20) #CAMBIAR
	ORIGINAL = 'Original'
	ORIGINAL_CHOICES = (
		('YES', "Original"),
		('NO', "No original"),
	)
	original = models.CharField(
		max_length=20,
		choices=ORIGINAL_CHOICES,
		default=ORIGINAL,
	)
	EXCHANGE='Intercambio'
	TRANSACTION_CHOICES = (
		('EXCHANGE', "Intercambio"),
		('SALE', "Venta"),
		('BOTH', "Ambos"),
	)
	transaction = models.CharField(
		max_length=20,
		choices=TRANSACTION_CHOICES,
		default=EXCHANGE,
	)
	price = models.PositiveIntegerField()
	comment = models.TextField()
	number_of_pages = models.PositiveIntegerField()
	picture = models.ImageField(upload_to='book/picture_books')

	def _str_(self):
		return self.user