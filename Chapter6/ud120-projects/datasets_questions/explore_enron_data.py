#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print 'Number of entries: ' + str(len(enron_data))
print 'Number of features: ' + str(len(enron_data[enron_data.keys()[0]]))

cpt = 0
for n in enron_data:
    cpt += enron_data[n]['poi']
        
print 'Total number of person of interest: ' + str(cpt)

for p in enron_data:
    if enron_data[p]['poi']:
        print p

import re

pattern = re.compile("^\((.)\)\b*([\w, ]+)\b*$")

cpt = 0
with open(r'..\final_project\poi_names.txt', 'r') as f:
    for line in f:
        match = pattern.match(line)
        if match:
            if match.group(1) == 'y':
                print match.group(1) + ' ' + match.group(2)
                cpt += 1

print 'Total POI: ' + str(cpt)

print 'PRENTICE JAMES total stock value: ' + str(enron_data['PRENTICE JAMES']['total_stock_value'])

def find_person(name, data):
    for i in data.keys():
        match = re.match('.*' + name + '.*', i, re.I)
        if match:
            return data[match.group(0)]
    return ''
        
print 'Message from Wesley Colwell: ' + str(find_person('Colwell', enron_data)['from_this_person_to_poi'])

print 'Stock option of Jeffrey K Skilling: ' + str(find_person('Skilling', enron_data)['exercised_stock_options'])

print 'Lay:' + str(find_person('Lay', enron_data)['total_payments'])
print 'Skilling:' + str(find_person('Skilling', enron_data)['total_payments'])
print 'Fastow:' + str(find_person('Fastow', enron_data)['total_payments'])

print ''

cpt_salary = 0
cpt_mail = 0
for p in enron_data.keys():
    if enron_data[p]['salary'] != 'NaN':
        cpt_salary += 1
    if enron_data[p]['email_address'] != 'NaN':
        cpt_mail += 1
print 'Number of person with a quatified salary: ' + str(cpt_salary)
print 'Number of person with a quatified mail: ' + str(cpt_mail)

cpt_totalPaiment = 0.0
cpt_totalPeople = 0.0
for p in enron_data.keys():
    if enron_data[p]['total_payments'] == 'NaN':
        cpt_totalPaiment += 1.0
    cpt_totalPeople += 1.0

print 'Percentage of people with NaN as total payment: ' + str(cpt_totalPaiment / cpt_totalPeople * 100)

cpt_totalPaiment = 0.0
cpt_totalPeople = 0.0
for p in enron_data.keys():
    if enron_data[p]['total_payments'] == 'NaN' and enron_data[p]['poi']:
        cpt_totalPaiment += 1.0
    cpt_totalPeople += 1.0

print 'Percentage of POI with NaN as total payment: ' + str(cpt_totalPaiment / cpt_totalPeople * 100)

cpt_totalPOI = 0.0
for p in enron_data.keys():
    if enron_data[p]['poi']:
        cpt_totalPOI += 1.0
print 'Total numer of POI: ' + str(cpt_totalPOI)

print 'Lay: ' + str(find_person('Lay', enron_data))


min_exercise_stock_option = 9999999
max__exercise_stock_option = 0
#field = 'exercised_stock_options'
field = 'salary'
for i in enron_data:
    if enron_data[i][field] != 0 and enron_data[i][field] < min_exercise_stock_option:
        min_exercise_stock_option = enron_data[i][field]
    elif enron_data[i][field] > max__exercise_stock_option \
        and enron_data[i][field] != 'NaN'\
        and i != 'TOTAL':
        max__exercise_stock_option = enron_data[i][field]

print 'Min = ' + str(min_exercise_stock_option)
print 'Max = ' + str(max__exercise_stock_option)