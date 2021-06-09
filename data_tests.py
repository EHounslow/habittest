import flask
from flask import Flask, render_template
from flask.globals import request
import pandas as pd
import matplotlib.pyplot as plt

download_url = "https://raw.githubusercontent.com/fivethirtyeight/data/master/college-majors/recent-grads.csv"

df = pd.read_csv(download_url)
pd.set_option("display.max.columns", None)
print(df.head())

df.plot(x="Rank", y=["P25th", "Median", "P75th"])
plt.savefig('./static/plot.png')
# plt.show()

#Matplotlib page
app = Flask(__name__)
@app.route('/matplot', methods=("POST", "GET"))
def mpl():
    if request.method == 'GET':
        return render_template('plot.html', PageTitle="Matplotlib", image="/static/plot.png")

app.run(host='0.0.0.0', port=81)