import pandas as pd
import dash
from dash import dcc, html
import plotly.graph_objs as go

# Load the CSV file
df = pd.read_csv('final_csv.csv')

# Convert CGPA columns to numeric
cgpa_cols = df.filter(like='CGPA').apply(pd.to_numeric, errors='coerce')
df[cgpa_cols.columns] = cgpa_cols

# Calculate the average CGPA for each semester
avg_cgpa = df.filter(like='CGPA').mean()

# Convert avg_cgpa to a dictionary
avg_cgpa_dict = avg_cgpa.to_dict()

# Create Dash app
app = dash.Dash(__name__)

# Define the layout
app.layout = html.Div([
    html.H1('Average CGPA Progression'),
    dcc.Graph(
        id='average-cgpa-graph',
        figure={
            'data': [
                {'x': list(avg_cgpa_dict.keys()), 'y': list(avg_cgpa_dict.values()), 'type': 'line', 'name': 'Average CGPA'},
            ],
            'layout': {
                'title': 'Average CGPA Progression',
                'xaxis': {'title': 'Semester'},
                'yaxis': {'title': 'Average CGPA'}
            }
        }
    )
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=False)
