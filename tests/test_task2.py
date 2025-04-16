import os
import pandas as pd
from dash_app.utils.task2_utils import calculate_sales

def test_sales_output_file():
    # 准备 mock 数据
    mock_data = [
        {"price": 5.0, "quantity": 2, "date": "2022-01-01", "region": "east"},
        {"price": 3.0, "quantity": 4, "date": "2022-01-01", "region": "west"}
    ]

    # 指定测试文件输出路径
    test_output_path = "output/test_output.csv"

    # 调用函数生成文件
    calculate_sales(mock_data, output_path=test_output_path)

    # ✅ 测试 1：文件是否写入成功
    assert os.path.exists(test_output_path), "输出文件不存在"

    # ✅ 测试 2：文件内容是否正确
    df = pd.read_csv(test_output_path)
    assert list(df.columns) == ["sales", "date", "region"]

    # ✅ 测试 3：销售额计算是否正确
    actual_sales = sorted(df["sales"].tolist())
    expected_sales = sorted([10.0, 12.0])

    assert actual_sales == expected_sales

    # ✅ 测试 4：总行数正确
    assert df.shape[0] == 2

    # 可选清理（开发时可删）
    # os.remove(test_output_path)