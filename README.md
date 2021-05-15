# CSGO Predictions
Intro: This repository was built for the second project of AiCore.

Purpose: The purpose of the project is predicting the outcome of a CSGO match based of ingame predictors such as time left in round,
money of each team,  health of each team e.t.c

Methodology: I started by importing the data and cleaning it. Then I did some base tests on different models (logistic regression, k-nearest neighbour and decision trees) to see which one would give me the best result initial result and continue from there. Decision trees gave me the best result so I continued with decision trees as the model. I then tested the model with train data against validation data and got overfitting on the data (train:0.9999136406768083, validation:0.7947305377704454). Using GridsearchCV and fine tuning hyperparameters I updated the model and ran it again and got a much better result with train and validation results being much closer to each other (train:0.8567048964812345, validation:0.8387436161189613). 

Since CSGO has a big betting/gambling scene I wanted to add a threshold function to bet on a round only if it has a high certainty if the terrorist team will win (since terrorist win is the variable I am predicting on). I applied this threshold and made a confusion matrix with this threshold in mind. I made a confusion matrix for both validation and test data. 

Results: Since the results of the project are realted to the gambling scene of CSGO we will look at the results with this lense in mind. Since we only care about predicting on the rounds where we are sure the terrorists will win we care about precision (this is true_positive/(true_positive + true_negative)) since true negatives are rounds we are betting wrongly on. For the test results this come to a precision score of 90%! This is also a fairly basic model so there is alot more that can be updated to it. 

Here is the link to the original dataset: https://www.kaggle.com/christianlillelund/csgo-round-winner-classification
