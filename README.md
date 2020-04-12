# Covid-19-Prediction
Covid-19 Detector which gives the probability of a patient being infected from covid-19 virus using Logistic regression model in Machine learning based on the symptoms.
Visit website below to use the webapp:
http://covidprediction.pythonanywhere.com

# Prerequisites

You must have Scikit Learn, Pandas, numpy (for Machine Leraning Model) and Flask, ninja2 (for API) installed.

Install requirements using : pip install -r requirements.txt

# Project Structure

This project has three major parts :

   1. training.py - This contains code for our Machine Learning model to predict the probability of a patient having COVID-19 infection based on training data in 'data.csv' file and updates 'model.pkl'.
   2. app.py - This contains Flask APIs that receives patient's symptoms details through GUI or API calls, computes the precited value based on our model and returns it.
   3. templates - This folder contains the HTML templates to allow user to enter patient sympyoms and displays the predicted infection probability. Templates in this project are : index.html, result.html, contact.html and about.html.
   
   
# Running the project

   1. Ensure that you are in the project home directory. Create the machine learning model by running below command -

            python training.py

      This would create a serialized version of our model into a file model.pkl

   2. Run app.py using below command to start Flask API

            python app.py

      flask will run on port 8000.

   3. Navigate to URL http://localhost:8000

      You should be able to view the homepage as below :
      
      ![Untitled1](https://user-images.githubusercontent.com/41967963/79075879-0cc04800-7d13-11ea-8949-87c23084b3a5.png)
      
   4. Enter valid values, select options in all the input boxes and hit Submit.

      If everything goes well, you should be able to see the predcited probability in terms of percentage(multiplied by 100) vaule on the 'result.html' page! 

![Untitled2](https://user-images.githubusercontent.com/41967963/79075943-9ec85080-7d13-11ea-9c3a-716018f3d1b6.png)
