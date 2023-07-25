# customer-conversion-prediction
In this project we will be predicting whether the customer will subscribe to the insurance or not from the insurance company. we have a marketing Dataset ,from that we are building a ML model to predict whether customers buy or not beforehand and specifically target via calls.

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
