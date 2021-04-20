from django.contrib import admin
from .models import Candle, Cart, Order


class CandleAdmin(admin.ModelAdmin):
	list_display = ('title', 'content', 'price', 'published')
	#list_display - последовательность имён полей, которые должны выводиться в списке записей
	list_display_link = ('title', 'content')
	#list_display_link - последовательность имён полей, которые должны быть преобразованы в гиперссылки, ведущие на страницу правки записи
	search_fields = ('title', 'content')
	#search_fields - последовательность имён полей, по которым должна выполняться фильтрация


class CartAdmin(admin.ModelAdmin):
	list_display = ('product', 'order', 'price', 'discount')
	list_display_link = ('product', 'order')
	search_fields = ('product', 'order')


class OrderAdmin(admin.ModelAdmin):
	list_display = ('order_id', 'date_order', 'time_order', 'price_order', 'payment_method', 'way_of_getting')
	list_display_link = ('payment_mathod', 'way_of_getting')
	search_fields = ('date_order', 'time_order', 'price_order', 'payment_method', 'way_of_getting')


admin.site.register(Candle, CandleAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(Order, OrderAdmin)