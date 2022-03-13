# for error response 
import requests

response=requests.get('https://api.github.com')
print(response)

# output- <Response [200]>


# open and reading json file of International Space Station iss
import requests 

response =requests.get(url="http://api.open-notify.org/iss-now.json")
print(response)
response.raise_for_status()       #here we are trying to display the error msg

data=response.json()    #here we are reading json file data
print(data)   

# output-
# <Response [200]>
# {'iss_position': {'latitude': '-43.5628', 'longitude': '10.1698'}, 'timestamp': 1647182324, 'message': 'success'}


# reading and display the samea json file but this time we are only extracting Latitude and Longitude

import requests 

response =requests.get(url="http://api.open-notify.org/iss-now.json")
print(response)
response.raise_for_status()      

data=response.json()    
print(data) 


longitude=data["iss_position"]["longitude"]
latitude=data["iss_position"]["latitude"]
iss_position=(longitude,latitude)
print(iss_position)

# output-
# <Response [200]>
# {'iss_position': {'latitude': '-33.0661', 'longitude': '26.8552'}, 'timestamp': 1647182594, 'message': 'success'}
# ('26.8552', '-33.0661')


# Covid 19 API Python
import requests 

response =requests.get(url="https://api.covid19india.org/data.json")
print(response)
response.raise_for_status()       

data=response.json()   
print(data)

# output-
# {'cases_time_series': [{'dailyconfirmed': '1', 'dailydeceased': '0', 'dailyrecovered': '0', 'date': '30 January 2020', 'dateymd': '2020-01-30', 'totalconfirmed': '1', 'totaldeceased': '0', 'totalrecovered': '0'}

# kanye.rest Api

import requests 

response =requests.get(url="https://api.kanye.rest")
print(response)
response.raise_for_status()       

data=response.json()   
print(data)

quote=data["quote"]
print(quote)

# ouput-
# <Response [200]>
# {'quote': "Let's be like water"}
# Let's be like water




