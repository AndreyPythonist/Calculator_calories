import requests
import json


response = requests.get(url="https://api.nal.usda.gov/fdc/v1/foods/search",
                        params={"query": "peanut", "api_key": "d5ESsIlZwyNXnuKgfGZqGgR5jmxMpiwgKhBEhO7Q"})
