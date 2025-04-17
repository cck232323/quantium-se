# from dash import html,dcc
# import dash_bootstrap_components as dbc

# layout = dbc.Container([
#     dbc.Row([
#         dbc.Col(html.H1("Hello Dash"), width=6),
#         dbc.Col(dbc.Button("Click me", id="btn", color="primary"), width=6),
#         dbc.Col(html.Div(id="output"))
        
#     ]),
#     dbc.Row([
#         dbc.Col(dbc.Button("Show Chart", id="run-btn", color="secondary"), width=3),
#         # dbc.Col(html.Div(id="output"))
#     ]),

#     # ✅ 新增折线图图表区域
#     dbc.Row([
#         dbc.Col(
#             dcc.Graph(id="sales-line-chart"),  # ← 关键图表 ID
#             width=12
#         )
#     ])
# ])
from dash import html, dcc
import dash_bootstrap_components as dbc

layout = dbc.Container([
    # ✅ 标题区
    dbc.Row([
        dbc.Col(html.H1("Pink Morsel Dashboard"), width=12, className="mb-3")
    ]),

    # ✅ 两个按钮横向对齐（整齐并有间距）
    dbc.Row([
        dbc.Col(dbc.Button("generate file", id="btn", color="primary", className="w-100"), width=3),
        dbc.Col(dbc.Button("display chart", id="run-btn", color="secondary", className="w-100"), width=3)
    ], className="mb-3"),

    # ✅ 输出文字区域，加 margin-bottom
    dbc.Row([
        dbc.Col(html.Div(id="output"), width=12)
    ], className="mb-3"),

    # ✅ 图表区域：设置最大宽度、中心对齐
    dbc.Row([
        dbc.Col(
            dcc.Graph(id="sales-line-chart"),
            width=12,
            style={"maxWidth": "1000px", "margin": "0 auto"}
        )
    ])
], fluid=True)