#importing necessary libraries
import numpy as np
import pandas as pd
from flask import Flask, request, render_template, url_for
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib

# Iitiated flask instance
app = Flask(__name__)

#home directory file to render index html file
@app.route('/')
def home():
    return render_template('home.html')