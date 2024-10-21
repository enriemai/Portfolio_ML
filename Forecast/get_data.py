import os, json, requests

#Sydney
location = (-33.88, 151.21)

#A decade
base_url = r"https://power.larc.nasa.gov/api/temporal/daily/point?parameters=T2M,T2M_MAX,T2M_MIN&community=RE&longitude={longitude}&latitude={latitude}&start=20140928&end=20240927&format=JSON"

api_request_url = base_url.format(longitude=location[1], latitude=location[0])

response = requests.get(url=api_request_url, verify=True, timeout=30.00)

content = json.loads(response.content.decode('utf-8'))
filename = response.headers['content-disposition'].split('filename=')[1]

output = r"./Forecast/Data"

filepath = os.path.join(output, filename)
with open(filepath, 'w') as file_object:
    json.dump(content, file_object)


