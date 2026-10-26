from sellix import Sellix
import requests

# EDIT: THIS IS NO LONGER IN DATE, SELLIX HAS HAD LEGAL TROUBLE AND IS NO LONGER ACTIVELY IN OPERATION
API_KEY = "example_api_key_placeholder"
merchant_name = "MERCHANT"

client = Sellix(API_KEY, merchant_name)
# dont run yet
product_uniqid = "ID"
product_payload = {
  "title": "TEST PRODUCT",
  "price": 7,
  "description": "TEST TEST TEST",
  "currency": "USD",
  "gateways": ["ETHEREUM", "LITECOIN", "BITCOIN"], 
  "type": "SERIALS",
  "serials": [
    "test1"
    "test2"
    "test3"]
}

try:
  client.update_product(product_uniqid, **product_payload)
except Sellix.SellixException as e:
  print(e)
