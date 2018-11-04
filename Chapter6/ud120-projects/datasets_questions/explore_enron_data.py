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
