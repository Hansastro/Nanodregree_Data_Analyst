#!/usr/bin/python

import sys
import pickle
import numpy as np
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.preprocessing import MinMaxScaler
sys.path.append("../tools/")

from feature_format import featureFormat, targetFeatureSplit
from tester import dump_classifier_and_data

### Task 1: Select what features you'll use.
### features_list is a list of strings, each of which is a feature name.
### The first feature must be "poi".
features_list = ['poi','salary', 'bonus', 'deferred_income', 'total_stock_value', 'exercised_stock_options', 'long_term_incentive', 'total_benefit', 'fraction_to_poi' ] # You will need to use more features

### Load the dictionary containing the dataset
with open("final_project_dataset.pkl", "br") as data_file:
    data_dict = pickle.load(data_file)

### Task 2: Remove outliers
# Remove of the mail address field
del  data_dict['TOTAL']

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

all_features_list = list(my_dataset['BECK SALLY W'].keys())
all_features_list.remove('email_address')
all_features_list.remove('poi')
all_features_list.insert(0, 'poi')

# --> Try the function SelectKBest, SelectPercentile, lasso of sklearn to reduce the number of features and see the impact

### Extract features and labels from dataset for local testing
data = featureFormat(my_dataset, features_list, sort_keys = True)
labels, features = targetFeatureSplit(data)

### Task 4: Try a varity of classifiers
# --> NaiveBayes
# --> Adaboost
# --> SVM
# --> Decision Tree
# --> PCA
### Please name your classifier clf for easy export below.
### Note that if you want to do PCA or other multi-stage operations,
### you'll need to use Pipelines. For more info:
### http://scikit-learn.org/stable/modules/pipeline.html

# Provided to give you a starting point. Try a variety of classifiers.
from sklearn import tree
clf = tree.DecisionTreeClassifier(max_depth=7, min_samples_leaf=2, min_samples_split=4)

### Task 5: Tune your classifier to achieve better than .3 precision and recall 
### using our testing script. Check the tester.py script in the final project
### folder for details on the evaluation method, especially the test_classifier
### function. Because of the small size of the dataset, the script uses
### stratified shuffle split cross validation. For more info: 
### http://scikit-learn.org/stable/modules/generated/sklearn.cross_validation.StratifiedShuffleSplit.html

# Example starting point. Try investigating other evaluation techniques!
def datasetSplit(features, labels, test_size=0.3, random_state=42):
    features = np.array(features)
    labels = np.array(labels)
    sss = StratifiedShuffleSplit(n_splits=1, test_size=test_size, random_state=random_state)
    for train_index, test_index in sss.split(features, labels):
        features_train, features_test = features[train_index], features[test_index]
        labels_train, labels_test = labels[train_index], labels[test_index]
    
    return features_train, features_test, labels_train, labels_test


scaler = MinMaxScaler()
features_selected = my_dataset
#features_rescaled = scaler.fit_transform(features_selected)
features_rescaled = features_selected

### Task 6: Dump your classifier, dataset, and features_list so anyone can
### check your results. You do not need to change anything below, but make sure
### that the version of poi_id.py that you submit can be run on its own and
### generates the necessary .pkl files for validating your results.

my_dataset = features_rescaled
dump_classifier_and_data(clf, my_dataset, features_list)