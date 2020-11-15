from django.shortcuts import render, redirect
from django.contrib import messages
import requests
import datetime
import xml.etree.ElementTree as ET
from .models import *
from .settings import *

def get_items(response):
    root = ET.fromstring(response.content)
    item_list = []
    for child in root.find('body').find('items'):
        elements = child.findall('*')
        data = {}
        for element in elements:
            tag = element.tag.strip()
            text = element.text.strip()
            #print(tag, text)
            data[tag] = text
        item_list.append(data)  
    return item_list

def home(request):
	return render(request, 'home.html', {})


def list_trade(request):
	try:
		if request.method == 'POST':
			name = request.POST['name']
			size = request.POST['size']
			nsize = 0
			if len(size) != 0:
				nsize = int(size)
			all_trade = AptTrade.objects.all().order_by('-date')
			param_trade = []
			for item in all_trade:
				cur_size = int(float(item.size))
				if item.name[:len(name)] == name:
					if nsize == 0:
						param_trade.append(item)
					elif cur_size == nsize:
						param_trade.append(item)

			return render(request, 'list_trade.html', context = {'apt_list':param_trade })
		else:
			all_trade = AptTrade.objects.all().order_by('-date')
			return render(request, 'list_trade.html', context = {'apt_list':all_trade })
	except Exception as e:
		apt = "Error..."
		return render(request, 'list_trade.html', {'api': apt, 'apt_list':[] })

def list_rent(request):
	try:
		if request.method == 'POST':
			name = request.POST['name']
			size = request.POST['size']
			nsize = 0
			if len(size) != 0:
				nsize = int(size)
			all_rent = AptRent.objects.all().order_by('-date')
			param_rent = []
			for item in all_rent:
				cur_size = int(float(item.size))
				if item.name[:len(name)] == name:
					if nsize == 0:
						param_rent.append(item)
					elif cur_size == nsize:
						param_rent.append(item)
			return render(request, 'list_rent.html', context = {'apt_list':param_rent })
		else:
			all_rent = AptRent.objects.all().order_by('-date')
			return render(request, 'list_rent.html', context = {'apt_list':all_rent })
	except Exception as e:
		apt = "Error..."
		return render(request, 'list_rent.html', {'api': apt, 'apt_list':[] })

def import_trade(request):
	if request.method != 'POST':
		return render(request, 'home.html', {})
	try:
		param_list = []
		request_month = request.POST['month']
		url ="http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTrade?"
		payload = "LAWD_CD=" + MY_GU_CODE + "&" + \
		          "DEAL_YMD=" + request_month + "&" + \
		          "serviceKey=" + API_SERVICE_KEY + "&" 
		          
		res = requests.get(url + payload)
		items_list = get_items(res)

		for item in items_list:
			if len(MY_DONGS) != 0 and item['법정동'] not in MY_DONGS:
				continue
			apt = AptTrade()
			apt.name = item['아파트']
			apt.price = item['거래금액']
			apt.dong = item['법정동']
			apt.size = item['전용면적']
			apt.built_year = item['건축년도']
			apt.floor = item['층']
			apt.month = request_month
			apt.date = '{:s}{:02d}{:02d}'.format(item['년'], int(item['월']), int(item['일']))
			apt.save()
			param_list.append(apt)

		count = len(param_list)
		messages.success(request, ("{0} 매매 데이터 {1}개 저장 되었습니다.".format(request_month, count)))
		return redirect(import_trade)
		#return render(request, 'import_trade.html', context = {'month':request_month, 'count':len(param_list)})
	except Exception as e:
		apt = "Error..."
		return render(request, 'import_trade.html', {'count':0 })

def import_rent(request):
	if request.method != 'POST':
		return render(request, 'home.html', {})

	try:
		param_list = []
		request_month = request.POST['month']
		url ="http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptRent?"
		payload = "LAWD_CD=" + MY_GU_CODE + "&" + \
		          "DEAL_YMD=" + request_month + "&" + \
		          "serviceKey=" + API_SERVICE_KEY + "&" 
		          
		res = requests.get(url + payload)
		items_list = get_items(res)

		for item in items_list:
			if len(MY_DONGS) != 0 and item['법정동'] not in MY_DONGS:
				continue
			apt = AptRent()
			apt.name = item['아파트']
			apt.deposit = item['보증금액']
			apt.rent_price = item['월세금액']
			apt.dong = item['법정동']
			apt.size = item['전용면적']
			apt.built_year = item['건축년도']
			apt.month = request_month
			apt.floor = item['층']
			apt.date = '{:s}{:02d}{:02d}'.format(item['년'], int(item['월']), int(item['일']))
			apt.save()
			param_list.append(apt)

		count = len(param_list)
		messages.success(request, ("{0} 전월세 데이터 {1}개 저장 되었습니다.".format(request_month, count)))
		return redirect(import_rent)

		#return render(request, 'import_rent.html', context = {'month':request_month, 'count':len(param_list)})
	except Exception as e:
		apt = "Error..."
		return render(request, 'import_rent.html', {'count':0 })


def delete_trade(request):
	if request.method != 'POST':
		return render(request, 'home.html', {})

	try:
		request_month = request.POST['month']
		all_trade = AptTrade.objects.all()
		count = 0
		for item in all_trade:
			if item.month == request_month:
				item.delete()
				count += 1
		messages.success(request, ("{0} 매매 데이터 {1}개 삭제되었습니다.".format(request_month, count)))
		return redirect(delete_trade)

	except Exception as e:
		apt = "Error..."
		return render(request, 'delete_trade.html', {'count':0 })

def delete_rent(request):
	if request.method != 'POST':
		return render(request, 'home.html', {})

	try:
		request_month = request.POST['month']
		all_rent = AptRent.objects.all()
		count = 0
		for item in all_rent:
			if item.month == request_month:
				item.delete()
				count += 1

		messages.success(request, ("{0} 전월세 데이터 {1}개 삭제되었습니다.".format(request_month, count)))
		return redirect(delete_rent)

		#return render(request, 'delete_rent.html', context = {'month':request_month, 'count':count})

	except Exception as e:
		apt = "Error..."
		return render(request, 'delete_rent.html', {'count':0 })
