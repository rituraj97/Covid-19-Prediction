# Covid-19-Prediction
Covid-19 Detector which gives the probability of a patient being infected from covid-19 virus using Logistic regression model in Machine learning based on the symptoms.

# Prerequisites

You must have Scikit Learn, Pandas, numpy (for Machine Leraning Model) and Flask, ninja2 (for API) installed.

Install requirements using : pip install -r requirements.txt

# Project Structure

This project has three major parts :

   1. training.py - This contains code for our Machine Learning model to predict the probability of a patient having COVID-19 infection based on training data in 'data.csv' file and updates 'model.pkl'.
   2. app.py - This contains Flask APIs that receives patient's symptoms details through GUI or API calls, computes the precited value based on our model and returns it.
   3. templates - This folder contains the HTML templates to allow user to enter patient sympyoms and displays the predicted infection probability. Templates in this project are : index.html, result.html, contact.html and about.html.
