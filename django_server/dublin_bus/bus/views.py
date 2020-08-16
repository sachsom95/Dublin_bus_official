from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.conf import settings
import pickle
import json
import pandas as pd 
import os
from .models import Currentweather, Forecastweather, Covid
from users.models import FavouriteDestination
from django.contrib.auth.models import User
# from rest_framework import serializers
from django.core import serializers

# sac: share logic here
def share(request,start_lat,start_lng,stop_lat,stop_lng,start,stop):
    position_data ={"start_lat":start_lat,
    "start_lng":start_lng,
    "stop_lat":stop_lat,
    "stop_lng":stop_lng,
    "start":start,
    "stop":stop}
    weather = Currentweather.objects.all()[0]
    # print(weather)
    forecast_raw = Forecastweather.objects.filter(weather_description__icontains='rain')[1:9]
    if forecast_raw:
        forecast = forecast_raw[0]
    else:
        forecast = forecast_raw
    # print(forecast)
    cov_info = Covid.objects.all().order_by('-Date')[0]
    # print(cov_info)
    cov_chart = Covid.objects.all().order_by('Date')
    # print(cov_chart)

    json_position_data = json.dumps(position_data)
    #context= {"position":json_position_data}
    return render(request, 'bus/index.html',{"position":json_position_data,'weather_info':weather, 'forecast':forecast, 'covid':cov_info,'covid_chart':cov_chart})

# end sac share logic

# Create your views here.
def home(request):
    weather = Currentweather.objects.all()[0]
    # print(weather)
    forecast_raw = Forecastweather.objects.filter(weather_description__icontains='rain')[1:9]
    if forecast_raw:
        forecast = forecast_raw[0]
    else:
        forecast = forecast_raw
    # print(forecast)
    cov_info = Covid.objects.all().order_by('-Date')[0]
    # print(cov_info)
    cov_chart = Covid.objects.all().order_by('Date')
    # print(cov_chart)
    if request.user.is_authenticated:
        destinations = FavouriteDestination.objects.filter(user=request.user)
        json_destinations = serializers.serialize('json', destinations)
    else:
        destinations = {}
        json_destinations = {}
    return render(request, 'bus/index.html',{ 'weather_info':weather, 'forecast':forecast, 'covid':cov_info,'covid_chart':cov_chart,'destinations':destinations,'json_destinations':json_destinations})

def tourism(request):
    return render(request, 'bus/tourism.html')

# @csrf_exempt
def prediction(request):
    # get lat & lng values for departure and arrival bus stops and the line chosen by google maps
    line,dep_lat,dep_lng,arr_lat,arr_lng,google_pred,time,day = request.GET['line'],request.GET['dep_lat'],request.GET['dep_lng'],request.GET['arr_lat'],request.GET['arr_lng'],request.GET['google_pred'],request.GET['time'],request.GET['day']

    ''' Because of the inconsistencies which result from using different data sources I am using latitudes and logituteds to match google maps chosen
    bus stops with bus stops in our data. The lats and longs wont be exactly the same so I am narrowing them down to 3 decimal places.
    after doing some research I decoverved that the third decimal place in a latitude or longitude signifies a difference of about 100 metres
    this means that by narrowing it down to three decimal places we will be using a bus stop that is in a 100 metre squared area of the stop goolge maps picked.
    This could be improved but I think it provides a good approximation for the time of the journey '''

    # narrowing google lat and longs as specified above
    dep_lat = dep_lat[0:6]
    dep_lng = dep_lng[0:6]
    arr_lat = arr_lat[0:6]
    arr_lng = arr_lng[0:6]

    # create dataframe out of csv with all the bus routes in our data
    df = pd.read_csv(os.path.abspath('bus/static/bus/routes_clean.csv'))

    # format the dataframe as necessary to compare the latitude and longitudes in our data with google maps data 
    df['longitude'] = df['longitude'].astype('str')
    df['latitude'] = df['latitude'].astype('str')
    df['longitude'] = df['longitude'].astype('str').str[0:6]
    df['latitude'] = df['latitude'].astype('str').str[0:6]

    # create a new df with only the routes containing the arrival or departure stops chosen by google maps
    true_df = df[(df['LINEID'] == line) & (((df['latitude'] == dep_lat) & (df['longitude'] == dep_lng)) | ((df['latitude'] == arr_lat) & (df['longitude'] == arr_lng)))]

    # search this new df of potential routes for one where BOTH departure and arrival bus stops are present and pick the first route where this is true
    potential_routes = []
    for key,value in true_df['ROUTEID'].value_counts().items():
        if value > 1:
            potential_routes.append(key)

    correct_route = 'N/A'
    for route in potential_routes:
        if len([(true_df['ROUTEID'] == potential_routes[0]) & ((true_df['latitude'] == dep_lat) & (true_df['longitude'] == dep_lng))]) > 0 and \
            len(true_df[(true_df['ROUTEID'] == potential_routes[0]) & ((true_df['latitude'] == arr_lat) & (true_df['longitude'] == arr_lng))]) > 0:
            correct_route = route
            break
    ''' honestly this way of chosing the route could be improved.
    it is picking any route with the start and end destination chosen by google maps without taking into account the number of stops between them
    this is because I am prioritising having our app make a prediction instead of using google prediction but maybe in the future we could add in some threshold
    i.e if google maps says there are 8 stops between departure and arrival the route we chose must havd 8 +/- 2 stops between them '''

    if correct_route != 'N/A':
        # if an appropriate model was found, load that model 
        with open(os.path.abspath('bus/static/bus/grad_boost_models/'+str(correct_route) +'_grad_boost_model.sav'), 'rb') as f:
            model = pickle.load(f)

            # get the percent of the route the journey will take
            total_stops_on_route = df[df['ROUTEID']==correct_route]['PROGRNUMBER'].max()
            dep_stop_on_route = df[(df['ROUTEID']==correct_route) & (df['latitude'] == dep_lat) & (df['longitude'] == dep_lng)]['PROGRNUMBER'].min()
            arr_stop_on_route = df[(df['ROUTEID']==correct_route) & (df['latitude'] == arr_lat) & (df['longitude'] == arr_lng)]['PROGRNUMBER'].max()
            num_stops = arr_stop_on_route - dep_stop_on_route
            percent_of_route = num_stops / total_stops_on_route * 100

            # make a prediction for how long the total bus route will take
            dummy_val_dict = {'ACTUALTIME_DEP':time,'temp':10,'wind_speed': 7,'Clouds':0,'Drizzle':0,'Fog':0,'Mist':0,'Rain': 0,'Smoke':0,'Snow':0,'Mon':0,'Sat':0,'Sun':0,'Thu':0,'Tue':0,'Wed':0}
            print(dummy_val_dict)
            print(day)
            dummy_values = [[]]
            dummy_val_dict['Clouds'] = 1
            # fridays have been dropped and are inferred from absence of other days
            if day != 'Fri':
                dummy_val_dict[day] = 1
            # add values for prediction to an array
            for key,value in dummy_val_dict.items():
                dummy_values[0].append(value)
            # make prediction
            prediction = model.predict(dummy_values)[0]

            # get a percentage of that prediction based on how much of the route will be travelled
            time_prediction = prediction / 100 * percent_of_route
    else:
        # if no appropriate model found use google time prediction
        time_prediction = google_pred

    # test_data = true_df.to_json()
    return JsonResponse({'prediction': time_prediction})

def addFavDest(request):
    current_user = request.user
    dest_name,dest_lat,dest_lng = request.GET['name'],request.GET['lat'],request.GET['lng']
    try:
        FavouriteDestination.objects.create(user_id= current_user.id, name=dest_name, lat=dest_lat,lng=dest_lng)
    except:
        result = "Something went wrong, if you have already added '"+ dest_name +"' as a favourite destination please delete it using the account page before replacing it"
    else:
        result = dest_name + " saved as favourite destination"
    return JsonResponse({'result': result})

def delFavDest(request):
    current_user = request.user
    dest_name = request.GET['name']
    print(dest_name)
    try:
        FavouriteDestination.objects.filter(user_id= current_user.id, name=dest_name).delete()
    except:
        result = "Something went wrong " + dest_name + " not removed"
    else:
        result = dest_name + " removed from favourite destinations"
    return JsonResponse({'result': result})




