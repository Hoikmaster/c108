import csv
import pandas as pd
import plotly.figure_factory as ff

df = pd.read_csv("data.csv")
fig = ff.create_distplot([df["Mobile Brand"].tolist()],["Mobile Brand"],show_hist=False)
fig.show()

df = pd.read_csv("data.csv")
fig = ff.create_distplot([df["Average Rating)"].tolist()],["Average Rating"],show_hist=False)
fig.show()