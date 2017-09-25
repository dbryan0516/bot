import gdax
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
	"asks": [price, size, number]

	where bids is price of buyable coins and
	asks is price of sellable coins

	e.g. bids is lower price
	"""
    return client.get_product_order_book(coin+'-USD', level=1)


def buyCoin(coin, usd, coinAmount):
	response = client.buy(price=usd, size=str(coinAmount), product_id=coin+'-USD')
	orderId = response['id']


def checkOrderStatus(orderId):
	response = client.get_order(orderId)
	return response['status']
