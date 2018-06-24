from django.contrib import admin
# from .models import User, Book
# from django.utils.safestring import mark_safe
#
#
# @admin.register(Book)
# class BookAdmin(admin.ModelAdmin):
#     list_display = (
#     		'title',
#         	'author',
#         	'editorial',
#         	'book_type',
#         	'genre',
#         	'language',
#         	'original',
#         	'transaction',
#         	'price',
#         	'comment',
#         	'number_of_pages',
#         	'picture',
#     )
#
#     def thumb(self, obj):
#         return mark_safe(u'<img src="%s" style="width:10px;height:10px;"/>' \
#             % (obj.picture.url))
#
#
# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = (
#     		'RUT',
#         	'commune',
#         	'phone',
#         	'fav_genre',
#     )
