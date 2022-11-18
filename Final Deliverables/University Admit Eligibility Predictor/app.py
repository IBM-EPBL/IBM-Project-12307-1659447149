import joblib
import numpy as np
model=joblib.load('model.pkl')
from flask import Flask, redirect, url_for, render_template, request
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")


@app.route("/y_predict", methods=['POST']) 
def y_predict():
    int_features=[float(x) for x in request.form.values()]
    final_features=[list(int_features)]
    prediction = model.predict(final_features)
    if prediction==True:        
        return render_template("chance.html")
    else:
        return render_template("noChance.html")

if __name__=='__main__':
    app.run()































    