import pandas as pd
import plotly.express as px  # (version 4.7.0)
import plotly.graph_objects as go

import dash  # (version 1.12.0) pip install dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

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

fig0 = px.scatter(df, x="Year", y="Age", color="Category", hover_name='Sex')
fig1 = px.scatter(df, x="Year", y="Age", color="Prize Share")
fig2 = px.bar(df, x="Year", y="Age", color='Category')
fig3 = px.box(df, x="Category", y="Age")
fig4 = px.box(df, x="Sex", y="Age", points='all')
fig5 = px.box(df, x="Sex", y="Age", color='Category')
fig6 = px.scatter(df, x="Year", y="Age", animation_frame="Year", color="Category", hover_name='Country',
                  size_max=45, range_x=[1905, 2016], range_y=[15, 90])

app.layout = html.Div(children=[
    # All elements from the top of the page
    html.Div([
        html.H1(children='Scatterplot : Years and Ages of Nobel Awardees '),

        html.Div(children='''
            Scatterplot generated over the years for all ages and genders, indexed by category names. 
        '''),

        dcc.Graph(
            id='graph1',
            figure=fig0
        ),
    ]),
    # New Div for all elements in the new 'row' of the page
    html.Div([
        html.H1(children='Scatterplot : Years and Ages of Nobel Awardees '),

        html.Div(children='''
            Scatterplot generated over the years for all ages and genders, indexed by prize share fractions. 
        '''),

        dcc.Graph(
            id='graph2',
            figure=fig1
        ),
    ]),
    html.Div([
        html.H1(children='Bar Graph : Years and Age '),

        html.Div(children='''
            Bar graph plotted over the years, indexed by category names. Colors represent categories annd number of bars represent number of awardees in a category for that year.
        '''),

        dcc.Graph(
            id='graph3',
            figure=fig2
        ),
    ]),

    html.Div([
        html.H1(children='Box Plot : Categories'),

        html.Div(children='''
            Box plot displaying age related vizualizations for all categories. Hover on the graphs for median, min, max, Q1 and Q3 values for each category.
        '''),

        dcc.Graph(
            id='graph4',
            figure=fig3
        ),
    ]),

    html.Div([
        html.H1(children='Box Plot : Gender'),

        html.Div(children='''
            Box plot displaying age related vizualizations for all genders. Hover on the graphs for median, min, max, Q1 and Q3 values for each gender.
        '''),

        dcc.Graph(
            id='graph5',
            figure=fig4
        ),
    ]),

    html.Div([
        html.H1(children='Box Plot : Gender based Visualizations over 5 Categories'),

        html.Div(children='''
            Box plot displaying gender related vizualizations over all categories. Hover on the graphs for median, min, max, Q1 and Q3 values for each category and gender.
        '''),

        dcc.Graph(
            id='graph6',
            figure=fig5
        ),
    ]),

    html.Div([
        html.H1(children='Scatter Plot with Animations'),

        html.Div(children='''
            Age and category related scatter plot over the years. Slide the bar for changes in visualizations over the years.
        '''),

        dcc.Graph(
            id='graph7',
            figure=fig6
        ),
    ]),

])

if __name__ == '__main__':
    app.run_server(debug=True)


