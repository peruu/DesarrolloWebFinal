from django.db import models

# Create your models here.
class User (models.Model):
	#Falta asociar uno o más libros
	RUT = models.CharField(max_length=15) #RUT
	commune = models.CharField(max_length=20)
	phone = models.PositiveIntegerField()
	NONE = 'Ninguno'
	FAV_GENRE_CHOICES = (
		('FANTASY', "Fantasía"),
		('FICTION', "Ficción"),
		('HORROR', "Terror"),
		('ROMANTIC', "Romantico"),
	)
	fav_genre = models.CharField(
		max_length=20,
		choices=FAV_GENRE_CHOICES,
		default=NONE,
	)

	def __str__(self):
		return self.RUT



class Book (models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
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
	genre = models.CharField(max_length=30) #CAMBIAR
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
	picture = models.ImageField(upload_to='media')

	def __str__(self):
		return self.title