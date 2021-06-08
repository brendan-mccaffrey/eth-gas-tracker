"""
http.client.HTTPSConnection: Used to grab data from sites that use TLS or SSL encryption.
"""
from http.client import HTTPSConnection

from importlib.util import spec_from_loader

from RequestB import DiscordRequest
from FtxClient import FtxClient

from json import loads

import pandas as pd

from openpyxl import Workbook
import os
from openpyxl import load_workbook

from os import error, path

from time import sleep

def makeRequest(client):

	request = DiscordRequest()

	# Generate the API location from the parameters.
	url = 'https://www.gasnow.org/api/v3/gas/price'

	# Make a request to retrieve the API data from Discord.
	response = request.sendRequest(url)

	# Convert the response data from serialized text to a dictionary.
	data = loads(response.read())

	prices = client.get_markets()
	eth_price = 0
	for d in prices:
		if d['name'] == 'ETH/USD':
			price = d['ask']

	data['data']['ETH Price'] = price

	df = pd.DataFrame(data['data'], index = [0])

	print(df)

	filepath = 'gasprices.csv'
	df.to_csv(filepath, mode='a', index = False, header=None)
	# filename = r'gas-prices.xlsx'
	# append_df_to_excel(filename, df)
	print(data['data'])

if __name__ == '__main__':

	api_key = '3bkp_y-Jydv1RNu4UepSOhm7LMCCiq42rUHhJfPr'
	api_secret = 'LZ2hfau4fzpGQbJD-omzv1GvR2UbNp22vwlo2Ixi'

	client = FtxClient(str(api_key), str(api_secret), None)
	while True:

		makeRequest(client)
		sleep(59)
	