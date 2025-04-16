from dash import Input, Output, callback
from dash_app.utils.task3_utils import load_grouped_sales_by_date
import plotly.express as px

@callback(
    Output("sales-line-chart", "figure"),
    Input("run-btn", "n_clicks"),  # 与任务2按钮复用（或另设按钮）
    prevent_initial_call=True
)
def render_sales_chart(n_clicks):
    df = load_grouped_sales_by_date()
    fig = px.line(df, x="date", y="sales", markers=True, title="按日期聚合的销售额")
    return fig