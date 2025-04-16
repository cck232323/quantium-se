# dash_app/utils.py
import os
import pandas as pd

def load_all_files(directory='data'):
    file_paths = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".csv"):
                file_paths.append(os.path.join(root, file))
    return file_paths

def filter_pink_morsel(file_paths):
    filtered_rows = []
    for file_path in file_paths:
        df = pd.read_csv(file_path)

        # 如果 price 是字符串（如 "$4.99"），先处理成 float
                # 无论什么 dtype 都统一清洗（更健壮）
        # df['price'] = df['price'].astype(str).replace('[\$,]', '', regex=True).astype(float)
        if df['price'].dtype == object:
            df['price'] = df['price'].replace('[\$,]', '', regex=True).astype(float)

        filtered = df[df['product'] == 'pink morsel']
        filtered_rows.extend(filtered.to_dict(orient='records'))
    return filtered_rows

def calculate_sales(filtered_rows, output_path='output/pink_morsel_output.csv'):
    df = pd.DataFrame(filtered_rows)
    df['sales'] = df['price'] * df['quantity']
    df = df[['sales', 'date', 'region']]
    # df.sort_values(['sales', 'date', 'region'], ascending=[False, True, True], inplace=True)
    df.sort_values(['date', 'region'], ascending=[True, True], inplace=True)
    df.to_csv(output_path, index=False)
    return output_path  # 返回路径，方便前端提示或下载
