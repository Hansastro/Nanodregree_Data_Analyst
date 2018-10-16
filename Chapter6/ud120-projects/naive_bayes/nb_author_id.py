#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
import time
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# Create the classifier
clf = GaussianNB()

startTime = time.time()

# Train the classifier
clf.fit(features_train, labels_train)

endTime = time.time()
print 'Classifer training execution time: {:.2f}s'.format(endTime - startTime)


startTime = time.time()

# Generated the prediction
pred = clf.predict(features_test)

endTime = time.time()
print 'Classifer prediction execution time: {:.2f}s'.format(endTime - startTime)

# Measure the accuracy of the prediction
accuracy = accuracy_score(labels_test, pred)

#print 'Accuracy: ' + str(accuracy)
print 'Accuracy: {:.2f}'.format(accuracy)

#########################################################


