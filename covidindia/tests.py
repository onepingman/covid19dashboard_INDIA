from django.test import TestCase
import requests
import json
#from apscheduler.schedulers import
# Create your tests here.
url = "https://covid-19-india2.p.rapidapi.com/details.php"
headers = {
    'x-rapidapi-host': "covid-19-india2.p.rapidapi.com",
    'x-rapidapi-key': "3386e1b99bmsh53ef1b437f02f08p1daeb3jsn59976e6cb1df"
    }
response = requests.request("GET", url, headers=headers)

data_in_json = json.loads(response.text)
print(data_in_json)

for i in data_in_json:
    print(i)
    print(data_in_json[i])