# Simple JSON transform routine
# Pull JSON records from a monitoring system
# Map Sensors of Interest to and transform
# Output new JSON objects
# Special thanks to Brian R for assistance at Boston Python Project Night

import json
import sys
# import requests
import logging
from pprint import pprint

# import file with all JSON objects
with open('data/format2.json') as json_data:
    ping = json.load(json_data)

app_a_sensors = [
    1, 3, 5
]

app_b_sensors = [
    1, 2, 4
]

all_sensors = set(app_a_sensors) | set(app_b_sensors)
for sensor_name in all_sensors:
    # GET sensor
    # Transform sensor
    # POST to interested apps
    pass

total = 0

for sensor in ping['sensors']:
    sys.stderr.write('Processing sensor {}\n'.format(sensor['sensor']))
    dashboard_sensor = {
        'applicationIdentifier': sensor['group'],
        'applicationCodes': [
            sensor['device'],
        ],
        'name': sensor['sensor'],
        'status': 'OK' if sensor['status'] == 'Pass' else 'ERROR',
         'messages': [
             sensor['lastvalue'],
        ]
    }
    total += 1
    # print(sensor)
    pprint(dashboard_sensor)
    jsontotal = len(sensor)
    sensortotal = total
    print('\nTotal dictionary items at top level', jsontotal)
    print('Total sensors processed...500 may be the limit??', sensortotal)

# Ping is now a dictionary with my
#  with open('refactored-sensors.json') as json_data:
#      postform = json.load(json_data)
#      json_data.close()




#print('inboundjson')
#print(ping)
#print('\nMaps to new json')
#  print(postform)

#x=type(ping)
#print('Type of loaded JSON objects is',x)