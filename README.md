# customer-conversion-prediction
In this project we will be predicting whether the customer will subscribe to the insurance or not from the insurance company. we have a marketing Dataset ,from that we are building a ML model to predict whether customers buy or not beforehand and specifically target  customers via calls.

From the observed analysis and visualization the ML model predicts the output whether the customer buys the insurance or not!

# Approach:
  -Read the data in csv format and do necessary preproceesing
  -replace the missing values
  -remove duplicates
  -remove outliers if needed
# DATA Visualization:
   -do Exploratory data Analysis
   -do distribution of Feature plot 
   -do Feature vs Target plot
# Encode:
   Encode the data
# Split:
   Split the data into train and test split using sklearn 
# Scale:
   Scale the data. 
   Scaling should be done onlyy on X_train and X_test.
   Y column is already in scaled format so scaling is not necessary.
# Balance the data:
  - since this is a n imbalanced data set balancing the data is mandatory.
  - Apply SMOTEENN technique to balance the data
  - Smote is used for oversamling the minorities
  - Enn is used for undersampling the majorities
# Model selection and Fiting
   -Apply each model on train test split and determine which model gives best Score
   - F1 score is the best evaluation metric for classification problem So F1 score is uded to calculate the scores
   - Determine feature importance and plot.
   - by doing this we can understand which feature plays the most important role in prediction of target variables.
  
  


pred.py file is for streamlit implementation of the model.

CONCLUSION:

      Based on the observation and visualization,The most important features are duration,age,day,month and job of an individual.
      After applying several machine learning models , here are the observation.

      Logistic Regression        -  F1 score : 48.10
      Knearest Neighbour         -  F1 score : 54.84 
      Decision Tree Classifier   -  F1 score : 53.40
      RandomForestClassifier     -  F1 score : 55.94
      BaggingClassifier          -  F1 score : 53.37
      XGBClassifier              -  F1 score : 58.95

      After using Ensemble learning method ,the scores are increasing.
      XG boost has Highest score so Xg boost is used for prediction.
      Although the Accuracy score of each model varies from 87% to 96%
      Accuracy is a bad evaluation metric for classification problem so 
      F1 score is chosen over Accuracy score.

      Also F1 score uses Harmonic mean while calculation where as in Accuracy, if false positve and false negative differs then precession and recall are checked. So F1 score is better for evaluation.

      After All the Machine learning Analysis we have done we came to Know that Based on this Analysis if the company calls the client and ask for buying the Insurance , The customer may buy the Insurance.
