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

