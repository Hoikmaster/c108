import csv
import pandas as pd
import plotly.figure_factory as ff

df = pd.read_csv("data.csv")
fig = ff.create_distplot([df["Average Rating)"].tolist()],["Average Rating"])
fig.show()
