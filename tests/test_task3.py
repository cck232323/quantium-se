from dash_app.utils.task3_utils import load_grouped_sales_by_date
import pandas as pd
import os
from dash_app.utils.task2_utils import calculate_sales
def test_grouped_sales_from_task2_output():
    task2_mock_data = [
        {"price": 5.0, "quantity": 2, "date": "2022-01-01", "region": "east"},   # 10.0
        {"price": 3.0, "quantity": 5, "date": "2022-01-01", "region": "west"},   # 15.0
        {"price": 4.0, "quantity": 5, "date": "2022-01-02", "region": "north"}   # 20.0
    ]

    output_path = "output/task3_test_output.csv"
    calculate_sales(task2_mock_data, output_path=output_path)

    df = load_grouped_sales_by_date(output_path)

    assert df.shape[0] == 2
    assert "date" in df.columns and "sales" in df.columns
    assert abs(df["sales"].sum() - 45.0) < 1e-6
    assert df["date"].dtype == "datetime64[ns]"

    os.remove(output_path)