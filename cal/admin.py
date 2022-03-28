from django.contrib import admin
from . models import Cal
class CalAdmin(admin.CalAdmin):
	list_display = ('sr', 'event', 'date', 'notes', 
	'Img_url')