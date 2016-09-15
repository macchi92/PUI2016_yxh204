import os
import sys
import json
import urllib.request as ulr

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + \
sys.argv[1] + "&VehicleMonitoringDetailLevel=calls&LineRef=B52"

response = ulr.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

bus_line = sys.argv[2]
buses = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

active_bus = 0

print("Bus Line : " + bus_line)
for i in range(len(buses)):
    if buses[i]['MonitoredVehicleJourney']['PublishedLineName'] == bus_line:
        active_bus += 1
        lat = buses[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
        lon = buses[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
        print("Bus " + str(active_bus) + " is at latitude " + str(lat) + " and longitude " + str(lon))