from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.conf import settings
import pickle
import json
import pandas as pd 
import os
from .models import Currentweather, Forecastweather, Covid


# Create your views here.
def home(request):
    return render(request, 'bus/index.html')

def tourism(request):
    return render(request, 'bus/tourism.html')

# @csrf_exempt
def prediction(request):
    # get lat & lng values for departure and arrival bus stops and the line chosen by google maps
    line,dep_lat,dep_lng,arr_lat,arr_lng,google_pred = request.GET['line'],request.GET['dep_lat'],request.GET['dep_lng'],request.GET['arr_lat'],request.GET['arr_lng'],request.GET['google_pred']

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
            dummy_values = [[84600.0,5.44,7.20,2924.0,1,0,0,0,0,0,0,0,0,0,0,1]]
            prediction = model.predict(dummy_values)[0]

            # get a percentage of that prediction based on how much of the route will be travelled
            time_prediction = prediction / 100 * percent_of_route
    else:
        # if no appropriate model found use google time prediction
        time_prediction = google_pred

    


    # test_data = true_df.to_json()
    
    return JsonResponse({'prediction': time_prediction})



def covid_and_weather(request):
    weather = Currentweather.objects.all()[0]
    # print(weather)
    forecast = Forecastweather.objects.all()
    # print(forecast)
    cov_info = Covid.objects.all().order_by('-Date')[0]
    # print(cov_info)
    cov_chart = Covid.objects.all().order_by('Date')
    # print(cov_chart)
    return render(request, 'bus/test.html',{ 'weather_info':weather, 'forecast':forecast, 'covid':cov_info,'covid_chart':cov_chart})
