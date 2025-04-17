from dash import Input, Output, State, callback
from dash_app.utils.task2_utils import load_all_files, filter_pink_morsel, calculate_sales

@callback(
    Output("output", "children"),
    Input("btn", "n_clicks"),
    prevent_initial_call=True
)
def run_task_2_sales_summary(n):
    file_paths = load_all_files('data')  # 只从 data/ 读
    filtered = filter_pink_morsel(file_paths)
    output_path = calculate_sales(filtered, output_path='output/pink_morsel_output.csv')
    return f"✅ Task completed, sales summary generated：{output_path}"
def update_output(n):
    return f"Button clicked {n or 0} times"