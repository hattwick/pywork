# Single PRTG sensor transform pipeline

# 1) Pull JSON records from a monitoring system
# 2) Map Sensors of Interest to new preferred format
# 3) Drop JSON records behind a web service for consuming applications to pick up

import json
import sys
import urllib2
from pprintimportpprint

#Retrieve and print static sensor

print('Test static single-sensor pipleine')
print('\nNative json response:\n')
macrosensor=json.load(urllib2.urlopen('https://serviceURL'))
printmacrosensor
sensor=macrosensor['sensordata']

# Result contained the dictionary we wanted inside of another dictionary.  This extracts the dictionary we want.

print('\nExtract sensor dictionary\n')
printsensor


#Modify sensor to new format

dashboard_sensor={
'applicationIdentifier':sensor['probename'],
'applicationCodes':[
sensor['uptime'],
sensor['downtime'],
sensor['updownsince']
],
'name':sensor['parentdevicename'],
'status':'PASS'ifsensor['statustext']=='Up'else'ERROR', #CAUTION: This is the critica field that we CHANGE
'messages':[
sensor['sensortype'],
]
}

# End of sensor processing


#Transformed sensor posting-Local feedback and file drop

print('\nSensor reformatted for new dashboard:\n')
pprint(dashboard_sensor)

filetag=dashboard_sensor['applicationIdentifier']

withopen('%s.json'%filetag,'wb')asjson_data:
json_data.write(json.dumps(dashboard_sensor))

print('\nPosted json file:')
print(filetag)


#-30-