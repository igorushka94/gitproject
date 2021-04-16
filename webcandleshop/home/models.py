from django.db import models


class Candle(models.Model):
	#id Товара
	""" Документация для класса Свеча(Candle) """
	#image = models.ImageField(help_text='280x475px', verbose_name='Изображение товара')
	title = models.CharField(max_length=50, verbose_name='Имя товара')
	content = models.TextField(null=True, blank=True, verbose_name='Описание аромата')
	price = models.FloatField(null=True, blank=True, verbose_name='Цена')
	published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')
	
	class Meta:
		verbose_name_plural = 'Товары'
		verbose_name = 'Товар'
		ordering = ['-published']


#class Cart(models.Model):
	#""" Документация класса Корзина(Cart) """
	#Товар
	#price = models.FloatField(null=True, blank=True, verbose_name='Цена')
	
	#class Meta:
		#verbose_name_plural = 'Клиенты'
		#verbose_name = 'Корзина'
		#ordering = ['-reg_date']


#class Client(models.Model):
	#""" Документация класса Клиент(Client) """
	#client_id = 
	#first_name = models.TextField(null=True, blank=True, verbose_name='Имя')
	#last_name = models.TextField(null=True, blank=True, verbose_name='Фамилия')
	#middle_name = models.TextField(null=True, blank=True, verbose_name='Отчество')
	#email_addr = models.EmailField(verbose_name='Email адресс')
	#reg_date = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата регистрации')
	#addr = models.TextField(null=True, blank=True, verbose_name='Адрес')

	#class Meta:
		#verbose_name_plural = 'Клиенты'
		#verbose_name = 'Клиент'
		#ordering = ['-reg_date']


#class Order(models.Model):
	#""" Документация класса Заказ(Order) """
	#order_id =
	#date_order = дата заказа
	#time_order = время заказа
	#Статус заказа
	#price_order = models.TextField(null=True, blank=True, verbose_name='Стоимость заказа')
	#payment_method = models.TextField(null=True, blank=True, verbose_name='Способ оплаты')
	#way_of_getting = models.TextField(null=True, blank=True, verbose_name='Способ получения')
	#login = тут покупатель

	#class Meta:
		#verbose_name_plural = 'Заказы'
		#verbose_name = 'Заказ'
		#ordering = ['-date_order']


#class OrderProduct(models.Model):
	#""" Документация класса Заказ-Продукт(OrderProduct) """
	#order_id = айди заказа
	#candle_id = айди товара

	#class Meta:
		#verbose_name_plural = 'Заказы-продукты'
		#verbose_name = 'Заказ продукт'