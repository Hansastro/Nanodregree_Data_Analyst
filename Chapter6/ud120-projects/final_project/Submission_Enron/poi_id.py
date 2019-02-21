#!/usr/bin/python

import pickle
import sys
import numpy as np
import pandas as pd
from sklearn.model_selection import StratifiedShuffleSplit, GridSearchCV
from sklearn.preprocessing import MinMaxScaler
sys.path.append("../tools/")

from feature_format import featureFormat, targetFeatureSplit
from tester import dump_classifier_and_data

### Task 1: Select what features you'll use.
### features_list is a list of strings, each of which is a feature name.
### The first feature must be "poi".
descision_tree_features_list = ['poi',
                 'exercised_stock_options',
                 'expenses',
                 'fraction_to_poi',
                 'total_benefit',
                 'shared_receipt_with_poi'
                 ]

best_features_list = [ 'poi',
                      'exercised_stock_options',
                      'total_stock_value',
                      'bonus',
                      'salary',
                      'total_benefit',
                      'fraction_to_poi']

features_list = descision_tree_features_list
# features_list = ['poi',
#                  'to_messages',
#                  'deferral_payments',
#                  'expenses',
#                  'deferred_income',
#                  'from_poi_to_this_person',
#                  'fraction_from_poi',
#                  'restricted_stock_deferred',
#                  'shared_receipt_with_poi',
#                  'loan_advances',
#                  'from_messages',
#                  'other',
#                  'director_fees',
#                  'bonus',
#                  'total_stock_value',
#                  'from_this_person_to_poi',
#                  'long_term_incentive',
#                  'restricted_stock',
#                  'salary',
#                  'total_payments',
#                  'fraction_to_poi',
#                  'exercised_stock_options',
#                  'total_benefit']

### Load the dictionary containing the dataset
with open("final_project_dataset.pkl", "r") as data_file:
    data_dict = pickle.load(data_file)

### Task 2: Remove outliers
del data_dict['TOTAL']
del data_dict['THE TRAVEL AGENCY IN THE PARK']

### Task 3: Create new feature(s)
# --> Total money (sum of all benefit total_payement + total_stock_value)
# --> fraction of mails to/from POI
### Store to my_dataset for easy export below.
my_dataset = data_dict


# Add the total benefit feature
for p in my_dataset:
    if my_dataset[p]['total_payments'] != 'NaN':
        total_payments = my_dataset[p]['total_payments']
    else:
        total_payments = 0
        
    if my_dataset[p]['total_stock_value'] != 'NaN':
        total_stock_value = my_dataset[p]['total_stock_value']
    else:
        total_stock_value = 0
    
    my_dataset[p]['total_benefit'] = total_payments + total_stock_value

def check_value(v):
    if v != 'NaN':
        return v
    else:
        return 0
    
# Add the mail to/from POI ratio
for p in my_dataset:
    to_message = check_value(my_dataset[p]['to_messages'])
    from_message = check_value(my_dataset[p]['from_messages'])
    from_poi_to_this_person = check_value(my_dataset[p]['from_poi_to_this_person'])
    from_this_person_to_poi = check_value(my_dataset[p]['from_this_person_to_poi'])
    
    if to_message == 0:
        my_dataset[p]['fraction_from_poi'] = 0
    else:
        my_dataset[p]['fraction_from_poi'] = from_poi_to_this_person / float(to_message)
    if from_message == 0:
        my_dataset[p]['fraction_to_poi'] = 0
    else:    
        my_dataset[p]['fraction_to_poi'] = from_this_person_to_poi / float(from_message)

### Extract features and labels from dataset for local testing
data = featureFormat(my_dataset, features_list, sort_keys = True)
labels, features = targetFeatureSplit(data)

### Task 4: Try a varity of classifiers
# Tried Algorithm:
# - Gaussian Naive Bayes
# - Decision Tree
# - KNN

### Please name your classifier clf for easy export below.
### Note that if you want to do PCA or other multi-stage operations,
### you'll need to use Pipelines. For more info:
### http://scikit-learn.org/stable/modules/pipeline.html

# Provided to give you a starting point. Try a variety of classifiers.

# Gaussian Naive Bayes
# ---------------------
from sklearn import tree
#from sklearn.naive_bayes import GaussianNB
#clf = GaussianNB()
# ---------------------

# Decision Tree
# -------------
from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier(splitter='best', max_leaf_nodes=5, min_samples_leaf=4, random_state=42, criterion='entropy', min_samples_split=2, max_depth=2)
#clf = DecisionTreeClassifier()
# -------------

# KNN
# ---
#from sklearn.neighbors import KNeighborsClassifier
#clf = KNeighborsClassifier(n_neighbors=6, leaf_size=1, algorithm='ball_tree', p=2)
#clf = KNeighborsClassifier()
# ---

### Task 5: Tune your classifier to achieve better than .3 precision and recall 
### using our testing script. Check the tester.py script in the final project
### folder for details on the evaluation method, especially the test_classifier
### function. Because of the small size of the dataset, the script uses
### stratified shuffle split cross validation. For more info: 
### http://scikit-learn.org/stable/modules/generated/sklearn.cross_validation.StratifiedShuffleSplit.html

# scaler = MinMaxScaler()
# features_rescaled = scaler.fit_transform(features)
# params = {'n_neighbors': [2,3,4,5,6,7,8,9,10],
#           'algorithm' : ['ball_tree', 'kd_tree', 'brute'],
#           'leaf_size': [1, 2, 3, 4, 5, 10, 20, 30, 40, 50],
#           'p': [1, 2, 3, 4, 5]}
# gridSearch = GridSearchCV(KNeighborsClassifier(), params)

# params = {'criterion': ['gini', 'entropy'],
#           'splitter': ['best', 'random'],
#           'max_depth': [None, 1, 2, 5, 10, 20],
#           'min_samples_split': [2, 3, 4, 5, 6, 7, 8, 9, 10],
#           'min_samples_leaf': [1, 2, 3, 4, 5, 6, 7, 8],
#           #'max_features': ['auto', 'sqrt', 'log2', None, 1, 3, 5, 7, 10],
#           'random_state': [42],
#           'max_leaf_nodes': [None, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#           }
# gridSearch = GridSearchCV(DecisionTreeClassifier(), params)

# gridSearch.fit(features_rescaled, labels)
# gridSearch.fit(features, labels)
# print(gridSearch.best_params_)

# Example starting point. Try investigating other evaluation techniques!
def datasetSplit(features, labels, test_size=0.3, random_state=42):
    features = np.array(features)
    labels = np.array(labels)
    sss = StratifiedShuffleSplit(n_splits=1, test_size=test_size, random_state=random_state)
    for train_index, test_index in sss.split(features, labels):
        features_train, features_test = features[train_index], features[test_index]
        labels_train, labels_test = labels[train_index], labels[test_index]
    
    return features_train, features_test, labels_train, labels_test


def scaleDict(dict_):
    '''
    Scale a dictionary, replace the NaN value by 0 and remove the email_address column if present

    parameter:
    - the dictionary of the dataset

    return:
    - the scaled dictionary
    '''
    # Convert the dictionay in a dataframe
    dataset = pd.DataFrame.from_dict(dict_, orient='index')

    # if the column email_address exists remove it (it is just text redondant with the name)
    if 'email_address' in dataset.columns:
        dataset.drop('email_address', axis=1, inplace=True)
    # Replace the NaN value by 0. Becareful in the pickel NaN is a string and not a type.
    dataset.replace('NaN', 0, inplace=True)

    # Rescale the data
    scaler = MinMaxScaler()
    features_rescaled = scaler.fit_transform(dataset)

    # recreate the dictionary and return it
    return pd.DataFrame(features_rescaled, index=dataset.index, columns=dataset.columns).to_dict(orient='index')

    data = featureFormat(dataset, feature_list, sort_keys = True)
    labels, features = targetFeatureSplit(data)

### Task 6: Dump your classifier, dataset, and features_list so anyone can
### check your results. You do not need to change anything below, but make sure
### that the version of poi_id.py that you submit can be run on its own and
### generates the necessary .pkl files for validating your results.

dump_classifier_and_data(clf, my_dataset, features_list)