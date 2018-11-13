# Identify Fraud from Enron Emails

# Workflow
1)	Get the data from the pickle file
2)	Cleanup the data (process the 'NaN' and remove the TOTAL entry)
3)	Check for ouliers
4)	Remove the outliers
5)	Select the features (SelectKBest, SelectPercentile or lasso of sklearn)
6)	Run a classifer
7)	Check the precision and recall 
8)	Tune the classifier parameter and iterate to step 6 with another classifer
9)	iterate to step 5 to try with another set of features

