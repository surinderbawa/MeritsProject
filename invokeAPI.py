import json

import requests
import sqlite3
import pandas  as pd
import numpy as py

requestURL = "http://127.0.0.1:5000/userdata/surinder"
resoutput = requests.request("GET",requestURL)
print(resoutput.status_code)
print(resoutput.json())

resoutput = requests.get(requestURL)
print(resoutput.status_code)
print(resoutput.json())

requestURL = "http://127.0.0.1:5000/userdata/surinder"
resoutput = requests.request("POST",requestURL)
print(resoutput.status_code)
print(resoutput.json())

requestURL = "http://127.0.0.1:5000/userdata/paramdeep"
resoutput = requests.request("POST",requestURL)
print(resoutput.status_code)
print(resoutput.json())

resoutput = requests.post(requestURL)
print(resoutput.status_code)
print(resoutput.json())

requestURL = "http://127.0.0.1:5000/userdata/paramdeep"
resoutput = requests.request("DELETE",requestURL)
print(resoutput.status_code)
print(resoutput.json())

resoutput = requests.delete(requestURL)
print(resoutput.status_code)
print(resoutput.json())
