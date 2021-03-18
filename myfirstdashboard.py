import pandas as pd
import plotly.express as px  # (version 4.7.0)
import plotly.graph_objects as go

import dash  # (version 1.12.0) pip install dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
external_stylesheets = ['https://cdn.jsdelivr.net/npm/water.css@2/out/water.css']


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

# Import and clean data (importing csv into pandas)
df = pd.read_csv("archive.csv")

df.rename(columns={"Birth Date": "Birthday", "Birth City": "Birth_city", "Laureate Type": "Laureate_type",
                   "Birth Country": "Country",
                   "Organization Name": "Organization", "Death Date": "Death_date", "Death Country": "Death_country"},
          inplace=True)

df.head()

# Slicing only the year out of Birthday and excluding month and day

df['Birth_Year'] = df['Birthday'].str[0:4]
df['Birth_Year'] = df['Birth_Year'].replace(to_replace="nan", value=0)
df['Birth_Year'] = df['Birth_Year'].apply(pd.to_numeric)
df['Age'] = df['Year'] - df['Birth_Year']

df.head()

fig0 = px.scatter(df, x="Year", y="Age", animation_frame="Year", color="Category", hover_name='Country',
                  size_max=45, range_x=[1905, 2016], range_y=[15, 90])
fig1 = px.scatter(df, x="Year", y="Age", color="Prize Share")
fig2 = px.bar(df, x="Year", y="Age", color='Category')
fig3 = px.box(df, x="Category", y="Age")
fig4 = px.box(df, x="Sex", y="Age", points='all')
fig5 = px.box(df, x="Sex", y="Age", color='Category')
fig6 = px.scatter(df, x="Year", y="Age", color="Category", hover_name='Sex')

app.layout = html.Div(children=[
    # All elements from the top of the page
    html.Div([
        html.H1(children='Age distribution over the years : By category '),

        html.Div(children='''
            Slide the bar from left to right to explore further.
            Hover on each datapoint to observe the specifics of a particular awardee.
        '''),

        dcc.Graph(
            id='graph0',
            figure=fig0
        ),
    ]),
    # New Div for all elements in the new 'row' of the page
    html.Div([
        html.H1(children='Age distribution over the years : By prize share'),

        html.Div(children='''
            Hover on the datapoints to explore them further. 
            Prize shares indicate the number of individuals who shared the prize in a particular year.
        '''),

        dcc.Graph(
            id='graph1',
            figure=fig1
        ),
    ]),
    html.Div([
        html.H1(children='Aggregate of category based awardees'),

        html.Div(children='''
           Hover on the bar graph to explore further.
           Colors represent categories and the number of bars represent the number of awardees in a category for a specific year.
        '''),

        dcc.Graph(
            id='graph2',
            figure=fig2
        ),
    ]),

    html.Div([
        html.H1(children='Age variation over categories'),

        html.Div(children='''
             Hover on the graphs for median, min, max, Q1 and Q3 values for each category.
        '''),

        dcc.Graph(
            id='graph3',
            figure=fig3
        ),
   
    ]),

    html.Div([
        html.H1(children='Gender based analysis'),

        html.Div(children='''
            These box plots display the distribution of age between male and female awardees. 
            Hover on the graphs for median, min, max, Q1 and Q3 values for each gender.
        '''),

        dcc.Graph(
            id='graph4',
            figure=fig4
        ),
  ]),

    html.Div([
        html.H1(children='Distribution of age for males and females over all categories'),

        html.Div(children='''
            Hover on the graphs for median, min, max, Q1 and Q3 values for each category and gender.
        '''),

        dcc.Graph(
            id='graph5',
            figure=fig5
        ),
    ]),

    html.Div([
        html.H1(children='Age distribution of Nobel awardees over the years '),

        html.Div(children='''
            Hover on the datapoints to explore them further. 
        '''),

        dcc.Graph(
            id='graph6',
            figure=fig6
        ),
    ]),

])

if __name__ == '__main__':
    app.run_server(debug=True)


