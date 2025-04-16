import pandas as pd

def load_grouped_sales_by_date(output_file="output/pink_morsel_output.csv"):
    df = pd.read_csv(output_file)
    df['date'] = pd.to_datetime(df['date'])
    grouped = df.groupby('date')['sales'].sum().reset_index()
    return grouped