import os
import sys
import json
import pandas as pd
import urllib.request as ulr

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + \
sys.argv[1] + "&VehicleMonitoringDetailLevel=calls&LineRef=B52"

response = ulr.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

bus_line = sys.argv[2]
buses = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

# Initialize columns
lat = []; lon = []
stop_name = []
stop_status = []

print("Latitude,Longitude,Stop Name,Stop Status")
for i in range(len(buses)):
    if buses[i]['MonitoredVehicleJourney']['PublishedLineName'] == bus_line:
        # Retrieve bus information
        lat_ = buses[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
        lon_ = buses[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
        stop_name_ = buses[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
        stop_status_ = buses[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']

        # Append to columns
        lat.append(lat_)
        lon.append(lon_)
        stop_name.append(stop_name_)
        stop_status.append(stop_status_)

        # Print according to format
        print(str(lat_)+','+str(lon_)+','+stop_name_+','+stop_status_)

bus_info = pd.DataFrame([lat,lon,stop_name,stop_status]).T
bus_info.columns = ["lat", "lon", "stop_name", "stop_status"]

filename = sys.argv[3]
bus_info.to_csv(filename, sep = ",")