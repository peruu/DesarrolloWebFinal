from django.urls import path
from book import views


urlpatterns = [
    path('',views.index,name="index"),
    path('/genres',views.add_genres,name="genres"),
]
