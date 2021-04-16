from django.http import HttpResponse
from django.shortcuts import render
from .models import Candle


def index(request):
	"""Выводит список товаров из БД Candle, с сортировкой по дате публикации"""
	#candles = Candle.objects.all()
	#return render(request, 'home/index.html', {'candles': candles})
	return HttpResponse("Страница домашняя для свечей")