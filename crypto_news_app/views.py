from django.shortcuts import render
import requests
import json
import pandas as pd
import datetime

def home(request):
	# Get Crypto Prices
	price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,USDT,USDC,DAI,BUSD,TUSD,FRAX,USDP,LUSD&tsyms=USD,EUR")
	price = json.loads(price_request.content)

	# Get Crypto News
	news_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN&categories=BTC,ETH,USDT,USDC,DAI,BUSD,TUSD,FRAX,USDP,LUSD")
	news = json.loads(news_request.content)
	return render(request, 'home.html', {'news': news, 'price': price,'time':datetime.datetime.now()})

def prices(request):
	if request.method == 'POST':
		# Get Crypto Prices
		quote = request.POST['quote']
		quote = quote.upper()
		crypto_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=" + quote + "&tsyms=USD,EUR")
		crypto = json.loads(crypto_request.content)
		return render(request, 'prices.html', {'quote': quote, 'crypto': crypto})
	else:
		notfound = "Enter a crypto currency symbol into the form above..."
		return render(request, 'prices.html', {'notfound': notfound})

def Ex_score(request):
    ##get exchange volume 
	exchange_list = ['Binance','Bitfinex','Bitstamp','Coinbase',
				     'HitBTC','Huobi','Kraken','OKEX','Poloniex','bybit','deribit','itBit']
	volume_dict ={}
	#Get total volume from the daily historical exchange data
	for e in exchange_list :
		volmue_request = requests.get(f"https://min-api.cryptocompare.com/data/exchange/histoday?={e}&tsym=usd&limit=1")
		volume = json.loads(volmue_request.content)
		volume_dict[e] =  volume['Data'][1]  
	pd.set_option('float_format', '{:f}'.format)
	volume_pd = pd.DataFrame.from_dict(volume_dict).T
	volume_pd['volume'] = volume_pd['volume'].apply(lambda x: '{:,.2f}'.format(x))
#	volume_pd['volume'] = volume_pd['volume'].astype(int)
	volume_pd.sort_values('volume',inplace=True,ascending=False)
	volume_pd['time'] = pd.to_datetime(volume_pd['time'],unit='s')
	print( volume_pd  )	
	return render(request, 'score.html', {'name': 'Total Daily Trading Volume by USD' , 'data': volume_pd.to_html(),'time':datetime.datetime.now()})

def report(request):
	return render(request, 'report.html')
