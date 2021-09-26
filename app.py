# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 11:40:38 2021

@author: LENOVO
"""

from flask import Flask, render_template, request
import pickle
from sklearn.preprocessing import StandardScaler

app=Flask(__name__)
model = pickle.load(open('medical.pkl', 'rb'))

@app.route("/", methods=["GET"])
def Home():
    return render_template('home.html')

standard_to = StandardScaler()
@app.route("/predict", methods= ["GET", "POST"])
def predict():
    if request.method == "POST":
        age=int(request.form["age"])
        sex=request.form["sex"]
        bmi=float(request.form["bmi"])
        children=int(request.form["children"])
        smoker=request.form["smoker"]
        region=request.form['region']
        if(region=='northwest'):
            northwest = 1
            southwest = 0
            southeast = 0
        elif(region == 'southwest'):
            northwest = 0
            southwest = 1
            southeast = 0
        else:
            northwest = 0
            southwest = 0
            southeast = 1       
            
            
        prediction=model.predict([[age, sex, bmi, children, smoker, northwest, southwest, southeast ]])
        
        output=round(prediction[0],2)
        return render_template("home.html", prediction_text="Your charge is ${}".format(output))
        
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug= True)
        