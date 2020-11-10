from django.db import models

class AptTrade(models.Model):
	name = models.CharField(max_length=32)
	price = models.CharField(max_length=12)
	size = models.CharField(max_length=12)
	dong = models.CharField(max_length=12)
	built_year = models.CharField(max_length=12)
	floor = models.CharField(max_length=4)
	month = models.CharField(max_length=8, default='', blank=True, null=True)
	date = models.CharField(max_length=24)
	cdate = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return str('{0}'.format(self.name))

class AptRent(models.Model):
	name = models.CharField(max_length=32)
	deposit =models.CharField(max_length=12)
	rent_price = models.CharField(max_length=12)
	size = models.CharField(max_length=12)
	dong = models.CharField(max_length=12)
	built_year = models.CharField(max_length=12)
	floor = models.CharField(max_length=4)
	month = models.CharField(max_length=8, default='', blank=True, null=True)
	date = models.CharField(max_length=24)
	cdate = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return str('{0}'.format(self.name))
