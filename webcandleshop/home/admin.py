from django.contrib import admin
from .models import Candle


class CandleAdmin(admin.ModelAdmin):
	list_display = ('title', 'content', 'price', 'published')
	list_display_link = ('title', 'content')
	search_fields = ('title', 'content')


admin.site.register(Candle, CandleAdmin)