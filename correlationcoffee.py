import pandas as pd
import plotly.express as px
import csv
import numpy as np

def getDataSource(data_path):
    coffee = []
    sleep = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            coffee.append(float(row["Coffee in ml"]))
            sleep.append(float(row["sleep in hours"]))
    return{"x": coffee, "y": sleep}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Coffee cups VS Sleep in hours: \n--->", correlation[0,1])

def setup():
    data_path = "CoffeeVSSleep.csv"
    datasource = getDataSource(data_path)
    findCorrelation(datasource)

setup()

import pandas as pd
import plotly.express as px

df = pd.read_csv("CoffeeVSSleep.csv")
fig = px.scatter(df, x = "Coffee in ml", y =  "sleep in hours")
fig.show()
