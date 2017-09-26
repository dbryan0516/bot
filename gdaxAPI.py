import gdax
from datetime import datetime
# gdax library https://github.com/danpaquin/gdax-python/

client = None


def initClient(key, b64secret, passphrase, useSandbox):
	if (client is None):
    	if (useSandbox):
        	client = gdax.AuthenticatedClient(
            	key, b64secret, passphrase, api_url="https://api-public.sandbox.gdax.com")
    	else:
        	client = gdax.AuthenticatedClient(key, b64secret, passphrase)
    	return client
    else:
    	return client


def invalidateClient():
	client = None


def getCoinPrice(coin):
	"""Returns order book in format 
	"bids": [price, size, number],
	"asks": [price, size, number],
	"time": time

	where bids is price of buyable coins and
	asks is price of sellable coins

	e.g. bids is lower price
	"""
	retunVal = client.get_product_order_book(coin+'-USD', level=1)
	retunVal['time'] = datetime.now()
    return retunVal


def buyCoin(coin, usd, coinAmount):
	"""
	Places a buy order given the coin name, USD amount to to spend, 
	and the coinMmount to buy

	Returns the orderID for the order placed; used to check status of order
	"""
	response = client.buy(price=usd, size=str(coinAmount), product_id=coin+'-USD')
	orderId = response['id']
	return orderId


def checkOrderStatus(orderId):
	"""
	Checks the status of an order given the ID
	"""
	# TODO: Consider using this for an order history sqlite table
	response = client.get_order(orderId)
	return response['status']
