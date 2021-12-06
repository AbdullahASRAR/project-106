import plotly.express as px
import csv
import numpy as np

def plotFigure(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df,x="Marks", y="Days")
        fig.show()

def getDataSource(data_path):
    marks = []
    days = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            marks.append(float(row["Marks"]))
            days.append(float(row["Days"]))

    return {"x" : marks, "y": days}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between marks vs days :-  \n--->",correlation[0,1])

def setup():
    data_path  = "mark-vs-days.csv"

    datasource = getDataSource(data_path)
    findCorrelation(datasource)
    plotFigure(data_path)

setup()