# 7.you're developing a program to analyze sensor data from Iot devices. Write a pyhton program to find the set of unique sensor types present inthe data.

def find_unique_sensor_types(sensor_data):
    unique_sensors=set()
    for reading in sensor_data:
        sensor_type=reading['type']
        unique_sensors.add(sensor_type)
    return unique_sensors


sensor_data=[{'id':1,'type':'temperature','value':22.5},
             {'id':2,'type':'humidity','value':60},
             {'id':3,'type':'pressure','value':101.3},
             {'id':4,'type':'temperature','value':23.1},
             {'id':5,'type':'humidity','value':50}]    

print(find_unique_sensor_types(sensor_data))
