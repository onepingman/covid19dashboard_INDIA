from django.shortcuts import render
from django.http import JsonResponse
import threading
from datetime import date
import requests
import json
from covidindia.models import DailyStateData, DailyTotalcases

def index(request):
    data = DailyTotalcases.objects.last()
    data = data.serialize()
    active = data["confirmed_corona_cases"]-data["recovered_corona_cases"]
    data["active_cases"] = active
    print(data)
    return render(request, "covidindia/index.html", data)

def indiamap(request):
    dict = {'Andaman and Nicobar Islands': 'AN', 'Andhra Pradesh': 'AP', 'Arunachal Pradesh': 'AR', 'Assam': 'AS',
            'Bihar': 'BR', 'Chandigarh': 'CH', 'Chhattisgarh': 'CT', 'Dadra and Nagar Haveli and Daman and Diu': 'DN',
            'Delhi': 'DL', 'Goa': 'GA', 'Gujarat': 'GJ', 'Haryana': 'HR', 'Himachal Pradesh': 'HP',
            'Jammu and Kashmir': 'JK','Jharkhand': 'JH', 'Karnataka': 'KA', 'Kerala': 'KL', 'Lakshadweep': 'LD', 'Madhya Pradesh': 'MP',
            'Maharashtra': 'MH','Manipur': 'MN', 'Meghalaya': 'ML', 'Mizoram': 'MZ', 'Nagaland': 'NL', 'Odisha': 'OD', 'Puducherry': 'PY',
            'Punjab': 'PB','Rajasthan': 'RJ', 'Sikkim': 'SK', 'Tamil Nadu': 'TN', 'Telengana': 'TS', 'Tripura': 'TR',
            'Uttarakhand': 'UK','Uttar Pradesh': 'UP', 'West Bengal': 'WB'}
    newdict={}
    obj = DailyTotalcases.objects.last()
    date = obj.date
    data = DailyStateData.objects.filter(date=date)
    data = [x.serialize() for x in data]
    for i in range(len(data)):
        inside_newdict = {}
        name = data[i]["state_name"]
        if name == "Ladakh":
            continue
        iso_code = dict[name]
        active_cases = data[i]["confirmed_corona_cases"] - data[i]["recovered_corona_cases"] - data[i]["deaths_corona_cases"]
        if active_cases > 100000:
            fill = "MAJOR"
        elif active_cases <= 100000 and active_cases > 40000:
            fill = "MEDIUM"
        elif active_cases <= 40000 and active_cases > 10000:
            fill = "MINOR"
        else:
            fill = "defaultFill"
        newdict[iso_code] = { "fillKey": fill, "numberOfThings": active_cases }
    return JsonResponse(newdict, safe=False)

def dailytrend(request,state):
    if state == "country":
        obj = DailyTotalcases.objects.all()
    else:
        obj = DailyStateData.objects.filter(state_name=state)

    obj = [x.serialize() for x in obj]
    newly_infected = []
    newly_recovered = []
    new_deaths = []
    dates = []
    for i in range(1, len(obj)):
        w = obj[i]["date"]
        dates.append(w)
        x = obj[i]["confirmed_corona_cases"] - obj[i - 1]["confirmed_corona_cases"]
        newly_infected.append(x)
        y = obj[i]["recovered_corona_cases"] - obj[i - 1]["recovered_corona_cases"]
        newly_recovered.append(y)
        z = obj[i]["deaths_corona_cases"] - obj[i - 1]["deaths_corona_cases"]
        new_deaths.append(z)
    data = [newly_infected, newly_recovered, new_deaths, dates]
    return JsonResponse(data, safe=False)

def datatable(request):
    obj = DailyTotalcases.objects.last()
    date = obj.date
    data = DailyStateData.objects.filter(date=date)
    data = [x.serialize() for x in data]
    return JsonResponse(data, safe=False)

###################################################################################

def myApiCall():
    today_date = date.today()  # present day date
    obj = DailyTotalcases.objects.all()
    length = len(obj)
    obj = obj.last().date  # find the latest date inside the database
    if length > 60:  # if the lenght of the object is above 60 we find the datasets with the oldest date and delete them because I am storing only 60 days data
        first_obj_date = DailyTotalcases.objects.first().date
        DailyTotalcases.objects.filter(date=first_obj_date).delete()
        DailyStateData.objects.filter(date=first_obj_date).delete()  # The data which is above 60 days will be deleted on successfully

    if obj != today_date:  # if the latest date from the database is same to the present date then we dont update the database
        url = "https://covid-19-india2.p.rapidapi.com/details.php"
        headers = {
            'x-rapidapi-host': "covid-19-india2.p.rapidapi.com",
            'x-rapidapi-key': "3386e1b99bmsh53ef1b437f02f08p1daeb3jsn59976e6cb1df"
        }

        try:
            response = requests.request("GET", url, headers=headers)
            data_in_json = json.loads(response.text)
            data_in_json = [value for value in data_in_json.values()]
            last_updated = data_in_json[0]  # the first dict inside data_json store the last updated date inside the apI json
            total_covid = data_in_json[
                len(data_in_json) - 1]  # the last dict stores the total overall cases of all the states

            latest = DailyTotalcases.objects.last().total_corona_cases  # if the api returns me with the same data then i wont be updating my database
            if latest != total_covid["total"]:  # to check if the data is same or not I do it by comparing lastest total cases in my DB with the total cases returned by the API
                # in the below code we add new data incrementally into our database
                DailyTotalcases.objects.filter(date=today_date).delete()  # First we save the total cases data
                d = DailyTotalcases(
                    date=today_date,
                    total_corona_cases=total_covid["total"],
                    confirmed_corona_cases=total_covid["confirm"],
                    recovered_corona_cases=total_covid["cured"],
                    deaths_corona_cases=total_covid["death"],
                )
                d.save()
                DailyStateData.objects.filter(date=today_date).delete()  # then we save the state wise data
                for i in range(1, len(data_in_json) - 1):
                    d = DailyStateData(
                        state_id=data_in_json[i]["slno"],
                        date=today_date,
                        total_corona_cases=data_in_json[i]["total"],
                        confirmed_corona_cases=data_in_json[i]["confirm"],
                        recovered_corona_cases=data_in_json[i]["cured"],
                        deaths_corona_cases=data_in_json[i]["death"],
                        state_name=data_in_json[i]["state"]
                    )
                    d.save()
        except:
            print("Something went wrong")

    threading.Timer(3600, myApiCall).start() # 3600 secs = 1hr this means this function will be called every 1 hr

myApiCall()


