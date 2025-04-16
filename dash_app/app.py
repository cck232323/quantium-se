# import dash
# from dash_app.layout import layout
# import dash_app.callbacks.task2_callbacks
# import dash_bootstrap_components as dbc
# # app = dash.Dash(__name__)
# app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
# app.layout = layout
# server = app.server
import dash
import dash_bootstrap_components as dbc
from dash_app.layout import layout

# 这一行是关键！！！一定不能漏
import dash_app.callbacks.task2_callbacks
print("✅ Callbacks registered!")  # 运行时是否出现
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = layout
server = app.server
