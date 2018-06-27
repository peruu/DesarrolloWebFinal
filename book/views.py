from django.shortcuts import render, redirect
from book.models import *
from book.forms import BookForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required



@login_required(login_url="/")
def index(request):
	object_list = Book.objects.filter(transaction='EXCHANGE') 
	data={}
	template_name = "book/index.html"
	user = User.objects.get(username=request.user.username)
	user_profile = UserProfile.objects.get(user=user)
	data['object_list'] = object_list
	return render(request, template_name, data)



@login_required(login_url="/")
def detail_book(request,id):
	template_name = "book/detail_book.html"
	data = {}
	book = Book.objects.get(id=id)
	print(book)
	data['detail_book']=book
	return render(request,template_name,data)



@login_required(login_url="/")
def view_book(request,id):
	template_name = "book/view_book.html"
	data = {}
	book = Book.objects.get(id=id)
	print(book)
	data['detail_book']=book
	return render(request,template_name,data)



@login_required(login_url="/")  
def list_book(request):
	object_list = Book.objects.all().order_by('-id')                #LISTA
	paginator = Paginator(object_list, 3)                           #PARA MOSTRAR 3 POR PAGINA
	page = request.GET.get('page')                                  #PASA SABER QUÉ PÁGINA EN F(X) DE REGISTROS
	data = {}
	template_name = 'book/list_book.html'
	try:
		b = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		b = paginator.page(1)
	except EmptyPage:
		# If page is out of rangAPRETARe (e.g. 9999), deliver last page of results.
		b = paginator.page(paginator.num_pages)
	data['object_list'] = object_list
	data['b'] = b
	return render(request, template_name, data)



@login_required(login_url="/")
def add_book(request):
	template_name = 'book/add_book.html'
	data={}
	if request.method == "POST":
		form = BookForm(request.POST, request.FILES)
		if form.is_valid():
			user = User.objects.get(username=request.user.username)
			user_profile = UserProfile.objects.get(user=user)
			user_book = UserBook.objects.get(user=user_profile)
			title = form.cleaned_data.get('title')
			author = form.cleaned_data.get('author')
			editorial = form.cleaned_data.get('editorial')
			book_type = form.cleaned_data.get('book_type')
			genre = form.cleaned_data.get('genre')
			language = form.cleaned_data.get('language')
			original = form.cleaned_data.get('original')
			transaction = form.cleaned_data.get('transaction')
			price = form.cleaned_data.get('price')
			comment = form.cleaned_data.get('comment')
			number_of_pages = form.cleaned_data.get('number_of_pages')
			picture = form.cleaned_data.get('picture')
			book = Book.objects.create(user=user_book,
				title=title,
				author=author,
				editorial=editorial,
				book_type=book_type,
				genre=genre,
				language=language,
				original=original,
				transaction=transaction,
				price=price,
				comment=comment,
				number_of_pages=number_of_pages,
				picture=picture)
			book.save
			return redirect('list_book')
	else:
		form = BookForm()
	data['form'] = form
	return render(request, template_name, data)



@login_required(login_url="/")
def edit_book(request,id):
	template_name = "book/add_book.html"
	data = {}
	book = Book.objects.get(id=id)
	if request.method == "GET":
		data['form'] = BookForm(instance=book)
	else:
		form_book= BookForm(request.POST,request.FILES, instance=book)
		if form_book.is_valid():
			form_book.save()
		return redirect('list_book')
	return render(request, template_name, data)



@login_required(login_url="/")
def delete_book(request,id):
	b = Book.objects.get(id=id)
	b.delete()
	return redirect('list_book')
#####USERBOOK#####


@login_required(login_url="/")
def view_sales(request):
	object_list = Book.objects.filter(transaction='SALE') 
	template_name = "book/view_sales.html"
	return render(request, template_name, {'object_list':object_list})


@login_required(login_url="/")
def view_both(request):
	object_list = Book.objects.all() 
	template_name = "book/view_both.html"
	return render(request, template_name, {'object_list':object_list})

