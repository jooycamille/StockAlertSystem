import requests
import datetime
import json

API_ENDPOINT = "https://api.polygon.io/v2/aggs/ticker/"
API_KEY = ""

def scheduledJob(stocksTicker,priceAlert) : 
    #send an API request to get the current stock price
    currentDate = datetime.datetime.now()
    #formattedCurrentDate = currentDate.strftime("%Y-%m-%d")
    formattedCurrentDate = "2023-03-31"
    composedUrl = API_ENDPOINT + stocksTicker + "/range/1/minute/" + formattedCurrentDate + "/" + formattedCurrentDate + "?adjusted=true&sort=desc&limit=1&apiKey=" + API_KEY
    currentPrice = requests.get(composedUrl)
    currentPrice = json.loads(currentPrice.text)["results"][0]["c"]

    if priceAlert == currentPrice:
        #we need to add the send email function
        print("the alert hit the current price")

scheduledJob("AAPL",164.9)
