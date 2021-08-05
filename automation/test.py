import json
import csv

##checks if there is a json value; if not, return the string none
def no_value(json_value):
    if json_value is None:
        return "None"
    else:
        return json_value

##check if there is a dictionary and if there is a key matching the value
##in the dict
def check_key(param, value):
    if param == 0:
        return 'None'
    elif param.get(value, 0) == 0:
        return 'None'
    else:
        return param[value]

##create list to hold header values for the csv
header = ['session_id', 'response_id', 'parkname', 'intent', 'location', 'time_stamp']

##create a csv file to write to
with open('sea_world_data.csv', 'w') as f:

    ##create a writer oject
    writer = csv.writer(f, lineterminator='\n')

    #write the head to the file
    writer.writerow(header)

    ##create a list that will hold all of the json objects
    new_list = []

    ##append json objects to the list
    with open('json.json') as f:
        for i in f:
          item = json.loads(i)
          new_list.append(item)

    #create list that will hold values of each row
    next_row = []

    interactions_list = []

    ##check and retrieve each value from each line and assign to variable for writing
    for line in new_list:
        session_id = no_value(line['session_id'])
        response_id = no_value(line['Response_id'])
        time_stamp = no_value(line['timestamp'])
        param = line.get('param', 0) ##make sure there is actually a param argument in this line
        park_name = check_key(param, 'parkname')
        intent = check_key(param, 'intent')
        location = check_key(param, 'location')

        ##assign values to list
        next_row = [session_id, response_id, park_name, intent, location, time_stamp]

        ##create a list of clean json objects
        interactions_list.append({'session_id': session_id, 'response_id': response_id, 
        'time_stamp': time_stamp, 'param': param, 'park_name': park_name, 'intent': intent, 
        'location':location})

        for line in interactions_list:
            print(line)
        
        ##write the values to the file
        writer.writerow(next_row)
    
    

