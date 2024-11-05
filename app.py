from pydoc import classname

import numpy as np
import pandas as pd
import plotly.graph_objects as go
import dash
from dash import html, dcc
from dash.dependencies import Input, Output

# Add the Bootstrap CDN URL and other external stylesheets if necessary
external_stylesheets = [
    {
        'href': 'https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css',
        'rel': 'stylesheet'
    },
    {
        'href': 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css',  # Font Awesome for icons
        'rel': 'stylesheet'
    }
]

# Dataframe
patients = pd.read_csv('IndividualDetails.csv')
total_cases = patients.shape[0]
active = patients[patients['current_status'] == 'Hospitalized'].shape[0]
recovered = patients[patients['current_status'] == 'Recovered'].shape[0]
deaths = patients[patients['current_status'] == 'Deceased'].shape[0]

# Options
statuses = patients['current_status'].unique().tolist()[:3]
options = [{'label': status, 'value': status} for status in statuses]
options.append({'label': 'All', 'value': 'All'})

# Initialize the Dash app with the external stylesheets
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Graph 1 (Line graph)
covid_df = pd.read_csv('covid_19_india.csv')
covid_df['Dates'] = pd.to_datetime(covid_df['Date'])
covid = covid_df.groupby('Dates')['Confirmed'].sum().reset_index()
covid = covid.sort_values(by='Dates')

trace = go.Scatter(x=covid['Dates'], y=covid['Confirmed'], mode='lines')
data = [trace]
layout = go.Layout(title="Day by Day Cases", xaxis_title='Date', yaxis_title='Total Cases')
fig = go.Figure(data=data, layout=layout)

# Age Group Data
agd = pd.read_csv('AgeGroupDetails.csv')
trace = go.Bar(x=agd['AgeGroup'], y=agd['TotalCases'])
data = [trace]
layout = go.Layout(title="AgeGroup v/s Case", xaxis_title='Age Group', yaxis_title='Total Cases')
fig2 = go.Figure(data=data, layout=layout)

# Layout of the app
app.layout = html.Div([
    html.H1("Covid-19 Pandemic", style={'color': '#ffffff', 'text-align': 'center', 'margin': '20px 0'}),

    # Row 1
    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    html.H3("Total Cases", className='text-light'),
                    html.H4(total_cases, className='text-light')
                ], className='card-body')
            ], className='card bg-danger')
        ], className='col-md-3 mb-4'),

        html.Div([
            html.Div([
                html.Div([
                    html.H3("Active Cases", className='text-light'),
                    html.H4(active, className='text-light')
                ], className='card-body')
            ], className='card bg-warning')
        ], className='col-md-3 mb-4'),

        html.Div([
            html.Div([
                html.Div([
                    html.H3("Recovered Cases", className='text-light'),
                    html.H4(recovered, className='text-light')
                ], className='card-body')
            ], className='card bg-success')
        ], className='col-md-3 mb-4'),

        html.Div([
            html.Div([
                html.Div([
                    html.H3("Deaths Cases", className='text-light'),
                    html.H4(deaths, className='text-light')
                ], className='card-body')
            ], className='card bg-primary')
        ], className='col-md-3 mb-4')
    ], className='row'),

    # Row 2
    html.Div([
        html.Div([
            html.Div([
                dcc.Graph(figure=fig)
            ], className='card-body')
        ], className='card col-md-8 mb-4'),

        html.Div([
            html.Div([
                dcc.Graph(figure=fig2)
            ], className='card-body')
        ], className='card col-md-4 mb-4')
    ], className='row'),

    # Row 3 (Dropdown and Bar graph)
    html.Div([
        html.Div([
            dcc.Dropdown(id='picker', options=options, value='All'),
            dcc.Graph(id='bar')
        ], className='card-body')
    ], className='card col-md-12 mb-4'),
], className='container mt-4')


# Callback for the bar chart
@app.callback(
    Output('bar', 'figure'),
    [Input('picker', 'value')]
)
def update_graph(selected_status):
    if selected_status == 'All':
        pbar = patients['detected_state'].value_counts().reset_index()
        pbar.columns = ['detected_state', 'count']
    else:
        npat = patients[patients['current_status'] == selected_status]
        pbar = npat['detected_state'].value_counts().reset_index()
        pbar.columns = ['detected_state', 'count']

    figure = {
        'data': [
            go.Bar(x=pbar['detected_state'], y=pbar['count'])
        ],
        'layout': go.Layout(
            title=f'Statewise Count for {selected_status}',
            xaxis_title="State",
            yaxis_title="Count",
            template="plotly_dark"
        )
    }
    return figure


if __name__ == '__main__':
    app.run_server(debug=True)
