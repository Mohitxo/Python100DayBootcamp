# API for sunrise and sunset with current system timing
# steps-

# 1.impporting requests
# 2.making variable that contains the Latitude and Longitude of the pune city you can change it accordingly 
# 3.making a dict name as parameter which contain imp parameter 
# 4.reading the data and printing it  


import requests
my_lat=18.520430
my_lng=73.856743
parameter={
    "lat":my_lat,
    "lng ":my_lng
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameter)
 

data=response.json()
print(data)

# print only sunrise and sunset timing
sunrise=data["results"]["sunrise"]
sunset=data["results"]["sunset"]
result=sunrise,sunset
print(result)
