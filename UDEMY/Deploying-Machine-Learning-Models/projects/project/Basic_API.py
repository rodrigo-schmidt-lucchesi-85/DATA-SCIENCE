from flask import Flask,request
import pandas as pd
import numpy as np
import pickle as pk

app = Flask(__name__)


@app.route('/')
def home():
    return "Welcome to Home"




if __name__ == '__main__':
    app.run()
