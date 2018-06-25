<<<<<<< HEAD
from django.shortcuts import render, redirect
# from book.models import Book, User
from book.forms import BookForm
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from django.http import HttpResponse
# from django.http import JsonResponse
# from django.template import RequestContext, loader
# from django.contrib import messages


# Create your views here.



#
# def inicio(request):
# 	template_name = "inicio.html"
# 	return render(request,template_name)
#
#
#
# def list_book(request):
# 	object_list = Book.objects.all().order_by('-id')				#LISTA
# 	paginator = Paginator(object_list, 3) 							#PARA MOSTRAR 3 POR PAGINA
# 	page = request.GET.get('page')									#PASA SABER QUÉ PÁGINA EN F(X) DE REGISTROS
#
# 	data = {}
# 	template_name = 'list_book.html'
#
# 	try:
# 		b = paginator.page(page)
# 	except PageNotAnInteger:
# 		# If page is not an integer, deliver first page.
# 		b = paginator.page(1)
# 	except EmptyPage:
# 		# If page is out of range (e.g. 9999), deliver last page of results.
# 		b = paginator.page(paginator.num_pages)
#
# 	return render(request, template_name, {'object_list':object_list, 'b':b})
#
#
#
def add_book(request):
	template_name = 'add_book.html'
	form = BookForm(request.POST or None)
	context = {'form':form}
	if request.method == "POST":
		form = BookForm(request.POST, request.FILES)

		if form.is_valid():
			form.save()
			print("Se guardó")
			return redirect('add_book')
	else:
		form = BookForm()
	return render(request, template_name, context)
#
#
# #HAY QUE HACER FUNCIONAR EL BOTÓN DE AGREGAR LIBRO EN LIST_BOOK
#
#
# def update_book(request,id):
# 	data = {}
# 	book = Book.objects.get(id=id)
# 	if request.method == "GET":
# 		data['form'] = BookForm(instance=book)
# 	else:
# 		data['form']= BookForm(request.POST,request.FILES, instance=book)
# 		b = data['form']
# 		if b.is_valid():
# 			b.save()
# 		return redirect('list_book')
# 	template_name = 'add_book.html'
# 	return render(request, template_name, data)
#
#
#
# def delete_book(request,id):
# 	b = Book.objects.get(id=id)
#
# 	if Book.objects.filter(id=id).exists():
# 		b = Book.objects.get(id=id)
# 		b.delete()
# 	else:
# 		print("No existe")
#
# 	return redirect('list_book')
#
#
# def prueba(request):
#     template_name = "prueba.html"
#     return render(request,template_name)
=======
from django.shortcuts import render
from book.models import *
from book.forms import *
from django.shortcuts import redirect

# Create your views here.
def index(request):
    template_name = "base.html"
    return render(request,template_name)

def add_genres(request):
    template_name="genres.html"
    data = {}
    #if request.method == 'POST':
    #form_genre = GenreForm(request.POST or None)
    #if form_genre.is_valid():
    #    form_genre.save()
    #    return redirect("base")
    #data['form'] = form_genre
    return render(request,template_name,data)

>>>>>>> fd0270f1a5aecbefe957dd25fc20d77e6031b0f0
