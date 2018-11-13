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
The analysis show that the data are quite widely distributed. To target the values which have an extrem value a z-Score calculation was performed. The results was check and all values are quite plausible. Just two values related to the number of mail sent are quite high. Possible but high. It is a point we have to keep in mind if this attribute is used as a feature.

# Add meta-features
Three meta-features are added:
- The total benefit (total_payments + total_stock_value)
- The from and to POI fractions (mail sent to/from POI divided by the total amount of from/to mail)

# Select the features
# Run a classifier
# Check the precision and recall 
# Validation
- estimate the performance on real world data
- help to detect overfitting

validation with RMSD root mean square deviation (test = training --> no overfit)
