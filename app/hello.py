from sre_constants import RANGE_UNI_IGNORE
from flask import Flask, render_template
import pandas as pd 
import plotly
import plotly.graph_objs as go

import pandas as pd
import numpy as np
import json

def create_plot():
    df = pd.read_csv('/Daily activity metrics.csv')
    fig = go.Figure()
    fig = fig.add_trace(go.Bar(x=df['Date'],y=df['Step count']))
    fig = fig.update_layout(title_text="My Step Count",xaxis={'rangeslider':{'visible':True}})
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON


app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/blog/')
def blog():
    return render_template('blog.html')

@app.route('/projects/')

def projects():
    bar = create_plot()
    return render_template('projects.html',plot = bar)


if __name__ == '__main__':
    app.run(debug=True)
