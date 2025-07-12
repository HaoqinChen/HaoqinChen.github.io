import pandas as pd
import json

def excel_to_json(excel_path, json_path, sheet_name=0):
    df = pd.read_excel(excel_path, sheet_name=sheet_name)
    df = df.dropna(how='all')
    df.columns = [str(col) for col in df.columns]
    # 如果有“日期”列，格式化为不带时分秒的字符串
    if '日期' in df.columns:
        df['日期'] = pd.to_datetime(df['日期']).dt.strftime('%Y-%m-%d')
    records = df.to_dict(orient='records')
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(records, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    excel_to_json("weight.xlsx", "weight.json")