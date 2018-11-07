#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.metrics import accuracy_score, precision_score, recall_score

import numpy as np

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)

#Split the data in training and test part
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, random_state=42, test_size=0.3)

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features_train, labels_train)

preds = np.array(clf.predict(features_test))

print("Accuracy: %f"%(accuracy_score(labels_test, preds)))

print("POIs predicted in the test set: %i"%(preds.sum()))
print("Number of people in the dataset: %i"%(len(preds)))
print("Number of true positif: %i"%(list(preds + labels_test).count(2)))
print("Precision: %f"%(precision_score(labels_test, preds)))
print("Recall Score: %f"%(recall_score(labels_test, preds)))
### your code goes here 


