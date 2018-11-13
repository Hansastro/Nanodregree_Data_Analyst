# Identify Fraud from Enron Emails

# Workflow
1) Get the data from the pickle file
2) Cleanup the data (process the 'NaN' and remove the TOTAL entry)
3) Check for ouliers
4) Remove the outliers
5) Select the features (SelectKBest, SelectPercentile or lasso of sklearn)
6) Test some classifers
7) Tune the classifier parameter
8) iterate to step 5 to try with other features
