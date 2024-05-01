# import pandas as pd
# import dash
# from dash import dcc, html
# import plotly.graph_objs as go

# # Load the CSV file
# df = pd.read_csv('final_csv.csv')

# # Convert CGPA columns to numeric
# cgpa_cols = df.filter(like='CGPA').apply(pd.to_numeric, errors='coerce')
# df[cgpa_cols.columns] = cgpa_cols

# # Calculate the average CGPA for each semester
# avg_cgpa = df.filter(like='CGPA').mean()

# # Convert avg_cgpa to a dictionary
# avg_cgpa_dict = avg_cgpa.to_dict()

# # Create Dash app
# app = dash.Dash(__name__)

# # Define the layout
# app.layout = html.Div([
#     html.H1('Average CGPA Progression'),
#     dcc.Graph(
#         id='average-cgpa-graph',
#         figure={
#             'data': [
#                 {'x': list(avg_cgpa_dict.keys()), 'y': list(avg_cgpa_dict.values()), 'type': 'line', 'name': 'Average CGPA'},
#             ],
#             'layout': {
#                 'title': 'Average CGPA Progression',
#                 'xaxis': {'title': 'Semester'},
#                 'yaxis': {'title': 'Average CGPA'}
#             }
#         }
#     )
# ])

# # Run the app
# if __name__ == '__main__':
#     app.run_server(debug=False)

# ME AND ADITYA'S

# import pandas as pd
# import dash
# from dash import dcc, html
# import plotly.graph_objs as go

# # Load the CSV file
# df = pd.read_csv('final_csv.csv')

# # Convert CGPA columns to numeric
# cgpa_cols = df.filter(like='CGPA').apply(pd.to_numeric, errors='coerce')
# df[cgpa_cols.columns] = cgpa_cols

# # Calculate the average CGPA for each semester
# avg_cgpa = df.filter(like='CGPA').mean()

# # Convert avg_cgpa to a dictionary
# avg_cgpa_dict = avg_cgpa.to_dict()

# # Create pass/fail counts for each semester
# pass_fail_counts = df.filter(like='PASS/FAIL').apply(pd.Series.value_counts)

# # Define custom colors
# pass_color = '#5588ff'  # Blue color for Pass
# fail_color = '#96bff1'   # Red color for Fail

# # Create Dash app
# app = dash.Dash(__name__)

# # Define the layout
# app.layout = html.Div([
#     html.Div([
#         html.H1('Pass/Fail Distribution by Semester', style={'text-align': 'center'}),
#         dcc.Graph(
#             id='pass-fail-graph',
#             figure={
#                 'data': [
#                     {'x': list(pass_fail_counts.columns), 'y': pass_fail_counts.loc['P'].values,
#                      'type': 'bar', 'name': 'Pass', 'marker': {'color': pass_color}},
#                     {'x': list(pass_fail_counts.columns), 'y': pass_fail_counts.loc['F'].values,
#                      'type': 'bar', 'name': 'Fail', 'marker': {'color': fail_color}}
#                 ],
#                 'layout': {
#                     'title': 'Pass/Fail Distribution by Semester',
#                     'xaxis': {'title': 'Semester', 'showgrid': False},
#                     'yaxis': {'title': 'Number of Students', 'showgrid': False},
#                     'barmode': 'stack',
#                     'plot_bgcolor': '#f0f0f0',  # Light gray background color
#                     'paper_bgcolor': '#f0f0f0',  # Light gray background color
#                     'font': {'color': '#333333'}  # Dark gray font color
#                 }
#             }
#         )
#     ]),

#     html.Div([
#         html.H1('Average CGPA Progression', style={'text-align': 'center'}),
#         dcc.Graph(
#             id='average-cgpa-graph',
#             figure={
#                 'data': [
#                     {'x': list(avg_cgpa_dict.keys()), 'y': list(avg_cgpa_dict.values()), 'type': 'line', 'name': 'Average CGPA'},
#                 ],
#                 'layout': {
#                     'title': 'Average CGPA Progression',
#                     'xaxis': {'title': 'Semester'},
#                     'yaxis': {'title': 'Average CGPA'}
#                 }
#             }
#         )
#     ])
# ])

# # Run the app
# if __name__ == '__main__':
#     app.run_server(debug=False)

# import pandas as pd
# import plotly.express as px
# import dash
# from dash import html, dcc
# import plotly.graph_objs as go

# # Load data
# df = pd.read_csv('final_csv.csv')

# # Convert CGPA columns to numeric
# cgpa_cols = df.filter(like='CGPA').apply(pd.to_numeric, errors='coerce')
# df[cgpa_cols.columns] = cgpa_cols

# # Calculate the average CGPA for each semester
# avg_cgpa = df.filter(like='CGPA').mean()

# # Convert avg_cgpa to a dictionary
# avg_cgpa_dict = avg_cgpa.to_dict()

# # Create pass/fail counts for each semester
# pass_fail_counts = df.filter(like='PASS/FAIL').apply(pd.Series.value_counts)

# # Define custom colors
# pass_color = '#5588ff'  # Blue color for Pass
# fail_color = '#96bff1'   # Red color for Fail

# # Create a bar chart using Plotly Express for Pass/Fail distribution
# pass_fail_fig = {
#     'data': [
#         {'x': list(pass_fail_counts.columns), 'y': pass_fail_counts.loc['P'].values,
#          'type': 'bar', 'name': 'Pass', 'marker': {'color': pass_color}},
#         {'x': list(pass_fail_counts.columns), 'y': pass_fail_counts.loc['F'].values,
#          'type': 'bar', 'name': 'Fail', 'marker': {'color': fail_color}}
#     ],
#     'layout': {
#         'title': 'Pass/Fail Distribution by Semester',
#         'xaxis': {'title': 'Semester', 'showgrid': False},
#         'yaxis': {'title': 'Number of Students', 'showgrid': False},
#         'barmode': 'stack',
#         'plot_bgcolor': '#f0f0f0',  # Light gray background color
#         'paper_bgcolor': '#f0f0f0',  # Light gray background color
#         'font': {'color': '#333333'}  # Dark gray font color
#     }
# }

# # Create a bar chart using Plotly Express for Highest CGPA per Semester
# highest_cgpas = {col: df[col].max() for col in cgpa_cols}
# cgpa_df = pd.DataFrame(list(highest_cgpas.items()), columns=['Semester', 'Highest CGPA'])
# cgpa_df['Semester'] = cgpa_df['Semester'].replace({'CGPA-': 'Semester '}, regex=True)  # Clean up semester names
# highest_cgpa_fig = px.bar(cgpa_df, x='Semester', y='Highest CGPA', title='Highest CGPA per Semester',
#                           text='Highest CGPA')
# highest_cgpa_fig.update_traces(texttemplate='%{text:.2f}', textposition='outside')
# highest_cgpa_fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')

# # Initialize the Dash app
# app = dash.Dash(__name__)

# # Define the layout of the app
# app.layout = html.Div([
#     html.H1("CGPA Dashboard"),
    
#     # Pass/Fail Distribution by Semester
#     html.Div([
#         html.H1('Pass/Fail Distribution by Semester', style={'text-align': 'center'}),
#         dcc.Graph(
#             id='pass-fail-graph',
#             figure=pass_fail_fig
#         )
#     ]),

#     # Average CGPA Progression
#     html.Div([
#         html.H1('Average CGPA Progression', style={'text-align': 'center'}),
#         dcc.Graph(
#             id='average-cgpa-graph',
#             figure={
#                 'data': [
#                     {'x': list(avg_cgpa_dict.keys()), 'y': list(avg_cgpa_dict.values()), 'type': 'line',
#                      'name': 'Average CGPA'},
#                 ],
#                 'layout': {
#                     'title': 'Average CGPA Progression',
#                     'xaxis': {'title': 'Semester'},
#                     'yaxis': {'title': 'Average CGPA'}
#                 }
#             }
#         )
#     ]),

#     # Highest CGPA per Semester
#     html.Div([
#         html.H1('Highest CGPA per Semester', style={'text-align': 'center'}),
#         dcc.Graph(
#             id='highest-cgpa-graph',
#             figure=highest_cgpa_fig
#         )
#     ])
# ])

# # Run the app
# if __name__ == '__main__':
#     app.run_server(debug=True)

# ADITYA PLUS ME PLUS GAURI'S CODE + HRISHABH
import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc
import plotly.graph_objs as go

data = pd.read_csv('final_csv.csv')

num_cols = ['CGPA-1','CGPA-2','CGPA-3','CGPA-4','CGPA-5','CGPA-6','CGPA-7']
data2 = data[num_cols]
# Convert object features to float, skipping NaN values
for col in num_cols:
    data2[col] = pd.to_numeric(data2[col], errors='coerce')

# Create a distribution plot for each feature
plt.figure(figsize=(16, 10))

for feature in num_cols:
    sns.displot(data2, x=feature, kde=True, color="skyblue", rug=True, bins=30)
    plt.title(f"Distribution of {feature}")
    plt.xlabel(feature)
    plt.ylabel("Density")
    plt.show()


# Load data
df = pd.read_csv('final_csv.csv')

# Convert CGPA columns to numeric
cgpa_cols = df.filter(like='CGPA').apply(pd.to_numeric, errors='coerce')
df[cgpa_cols.columns] = cgpa_cols

# Calculate the average CGPA for each semester
avg_cgpa = df.filter(like='CGPA').mean()

# Convert avg_cgpa to a dictionary
avg_cgpa_dict = avg_cgpa.to_dict()

# Create pass/fail counts for each semester
pass_fail_counts = df.filter(like='PASS/FAIL').apply(pd.Series.value_counts)

# Define custom colors
pass_color = '#5588ff'  # Blue color for Pass
fail_color = '#96bff1'   # Red color for Fail

# Create a bar chart using Plotly Express for Pass/Fail distribution
pass_fail_fig = {
    'data': [
        {'x': list(pass_fail_counts.columns), 'y': pass_fail_counts.loc['P'].values,
         'type': 'bar', 'name': 'Pass', 'marker': {'color': pass_color}},
        {'x': list(pass_fail_counts.columns), 'y': pass_fail_counts.loc['F'].values,
         'type': 'bar', 'name': 'Fail', 'marker': {'color': fail_color}}
    ],
    'layout': {
        'title': 'Pass/Fail Distribution by Semester',
        'xaxis': {'title': 'Semester', 'showgrid': False},
        'yaxis': {'title': 'Number of Students', 'showgrid': False},
        'barmode': 'stack',
        'plot_bgcolor': '#f0f0f0',  # Light gray background color
        'paper_bgcolor': '#f0f0f0',  # Light gray background color
        'font': {'color': '#333333'}  # Dark gray font color
    }
}

# Create a bar chart using Plotly Express for Highest CGPA per Semester
highest_cgpas = {col: df[col].max() for col in cgpa_cols}
cgpa_df = pd.DataFrame(list(highest_cgpas.items()), columns=['Semester', 'Highest CGPA'])
cgpa_df['Semester'] = cgpa_df['Semester'].replace({'CGPA-': 'Semester '}, regex=True)  # Clean up semester names
highest_cgpa_fig = px.bar(cgpa_df, x='Semester', y='Highest CGPA', title='Highest CGPA per Semester',
                          text='Highest CGPA')
highest_cgpa_fig.update_traces(texttemplate='%{text:.2f}', textposition='outside')
highest_cgpa_fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')

# Extract columns containing 'PASS/FAIL' in their name
pass_fail_columns = [col for col in df.columns if 'PASS/FAIL' in col]
# Visualization : Violin Plot of CGPA Distribution
fig_violin_plot = px.violin(df.melt(value_vars=numeric_cols), y='value',
                             facet_col='variable', box=True, title='CGPA Distribution (Violin Plot)')

# Initialize the Dash app
app = Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    html.H1("CGPA Dashboard"),
    
    # Pass/Fail Distribution by Semester
    html.Div([
        html.H1('Pass/Fail Distribution by Semester', style={'text-align': 'center'}),
        dcc.Graph(
            id='pass-fail-graph',
            figure=pass_fail_fig
        )
    ]),

    # Average CGPA Progression
    html.Div([
        html.H1('Average CGPA Progression', style={'text-align': 'center'}),
        dcc.Graph(
            id='average-cgpa-graph',
            figure={
                'data': [
                    {'x': list(avg_cgpa_dict.keys()), 'y': list(avg_cgpa_dict.values()), 'type': 'line',
                     'name': 'Average CGPA'},
                ],
                'layout': {
                    'title': 'Average CGPA Progression',
                    'xaxis': {'title': 'Semester'},
                    'yaxis': {'title': 'Average CGPA'}
                }
            }
        )
    ]),

    # Highest CGPA per Semester
    html.Div([
        html.H1('Highest CGPA per Semester', style={'text-align': 'center'}),
        dcc.Graph(
            id='highest-cgpa-graph',
            figure=highest_cgpa_fig
        )
    ]),
    
    # Pass/Fail Pie Charts
    html.Div([
        html.H1("CGPA Pass/Fail Distribution Dashboard"),
        html.Div([
            dcc.Graph(
                id=f'pie-chart-{i}',
                figure=px.pie(df, names=column, title=f'{column} Distribution')
            ) for i, column in enumerate(pass_fail_columns, start=1)
        ])
    ]),
    # Visualization : Violin Plot of CGPA Distribution
    html.Div([
        html.H2('CGPA Distribution (Violin Plot)'),
        dcc.Graph(
            id='cgpa-violin-plot',
            figure=fig_violin_plot
        )
    ])
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
