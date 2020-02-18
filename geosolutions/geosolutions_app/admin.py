from django.contrib import admin
from . import models

@admin.register(models.Point)
class PointAdmin(admin.ModelAdmin):
	list_display = ['pk', 'x', 'y', ]
	list_display_links = ['pk', 'x', 'y', ]

@admin.register(models.Search)
class SearchAdmin(admin.ModelAdmin):
	list_display = [
		'search_x',
		'search_y',
		'operation',
		'points',
	]
	list_display_links = [
		'search_x',
		'search_y',
		'operation',
		'points',
	]

