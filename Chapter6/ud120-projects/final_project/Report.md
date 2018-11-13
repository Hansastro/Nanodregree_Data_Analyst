# Identify Fraud from Enron Emails

# Workflow
1) Get the data from the pickle file
2) Cleanup the data (process the 'NaN' and remove the TOTAL entry)
3) Check for ouliers
4) Remove the outliers
5) Add meta-features
3) Select the features (SelectKBest, SelectPercentile or lasso of sklearn)
6) Run a classifer
7) Check the precision and recall 
8) Tune the classifier parameter and iterate to step 6 with another classifer
9) Iterate to step 5 to try with another set of features

# Cleanup the data
We have here two sort of non valid data:
- The 'NaN' data which is a text format and does not work with digital values. All 'NaN' value will be replaced by 0. This is done by the function featureFormat with the paramater 'remove_NaN' which is true per default.  
- The TOTAL entry which sum each columns of the dataset. This entry must be removed.

In the dataset, there is a field "email address". This information is not usefull to identify the POIs (it is unique for each people). This field should be removed.

# Check for outliers


