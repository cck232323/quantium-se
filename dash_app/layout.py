from dash import html

# layout = html.Div([
#     html.H1("Hello Dash"),
#     html.Button("Click me", id="btn"),
#     html.Div(id="output")
# ])
import dash_bootstrap_components as dbc

layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("Hello Dash"), width=6),
        dbc.Col(dbc.Button("Click me", id="btn", color="primary"), width=6)
    ]),
    html.Div(id="output")
])