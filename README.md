
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

# Dublin Bus Project
NOTE : FOR ALL THINGS TECH LOOK AT OUR 
[Wiki!!](https://github.com/sachsom95/Dublin_bus_official/wiki)
<br>Test coverage : 95%

### This is Dublin Buses a webapp Every Dubliners crave for. 
Get the best bus journey predictions modeled on 2018 Dublin bus dataset.
![Dublin Bus](https://github.com/sachsom95/Dublin_bus_official/blob/master/readme_content/intro.gif)

### Have leap card and dont know the balance?
Link leap card to the app and check your balance and bus all in same place bonus: cool avatar included :)
![Leap card](https://github.com/sachsom95/Dublin_bus_official/blob/master/readme_content/login.gif)

### wanna share bus route from "Dún Laoghaire" to "clonskeagh" to your just arrived foreign friend who doesn't know how to type Irish places.
Use the share my trip feature and send the link to them with everything pre-written yaaay!.
![Sharable link](https://github.com/sachsom95/Dublin_bus_official/blob/master/readme_content/sharable_link.gif)

### Keep you favourite locations saved.
No need to search guineess store house all the time.
![Sharable link](https://github.com/sachsom95/Dublin_bus_official/blob/master/readme_content/fav.gif)

### Popular tourist destinations all in single click of button.
Thats right no need to search for Guninness store house.
![More stuff](https://github.com/sachsom95/Dublin_bus_official/blob/master/readme_content/tourism.gif)

### Get the latest Covid data and decide if you want to use the bus.
Hope this feature doesn't last long.
![More stuff](https://github.com/sachsom95/Dublin_bus_official/blob/master/readme_content/covid.gif)

### Android webview app.
No need to access the app via browser use the APK

### Get latest tweets from dublin bus and covid updates right from the app.

### APP architecture
![Architecture](https://github.com/sachsom95/Dublin_bus_official/blob/master/Dublin_bus_architecture.png)




### How to run app locally

Here are the steps to properly run the application:<br>
• Create conda environment<br>
• conda create --name bus_app python=3.7<br>
• conda activate bus_app<br>
• Go inside the folder that was downloaded where there should be a requiments.txt<br>
• pip install -r requirments.txt<br>
• go inside Dublin_bus_official-3.0/django_server/dublin_bus/bus on your terminal<br>
• run the three scraper scripts Currentweather_update.py, Forecastweather_update.py,<br>
Covid_update.py in Dublin_bus_official-3.0/django_server/dublin_bus/bus using python
'filename'<br>
• (because we automaticly and timely run these three scrapers on the server with cronjob
of linux server. you have to run these there python file to get the latest data into data
base)<br>
• Do the command “cd ..” to go back into the previous directory dublin_bus/ where
manage.py lies<br>
• Run “python manage.py runserver”<br>
• Remember you need to get your own google maps api with, placesAPI, distance matrix enabled<br>


