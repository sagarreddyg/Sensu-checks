import requests
from datetime import datetime

datetime1 = "2019-01-24T00:21:41-05:00"
date = datetime1[:10]
time = datetime1[11:]
print(date)
print(time)
