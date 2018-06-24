from django.contrib import admin
from book.models import *
# Register your models here.
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user",)
@admin.register(UserBook)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user",)

