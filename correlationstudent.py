import pandas as pd
import plotly.express as px
import csv
import numpy as np

def getDataSource(data_path):
    marks = []
    days = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            marks.append(float(row["Marks In Percentage"]))
            days.append(float(row["Days Present"]))
    return{"x": marks, "y": days}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Marks in Percentage VS Days Present: \n--->", correlation[0,1])

def setup():
    data_path = "StudentMarksVSDaysPresent.csv"
    datasource = getDataSource(data_path)
    findCorrelation(datasource)

setup()

import pandas as pd
import plotly.express as px

df = pd.read_csv("StudentMarksVSDaysPresent.csv")
fig = px.scatter(df, x = "Marks In Percentage", y =  "Days Present")
fig.show()
