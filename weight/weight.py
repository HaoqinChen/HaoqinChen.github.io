import pandas as pd
import json
import os

def csv_to_json(csv_path="weight.csv", json_path="weight.json"):
    try:
        print(f"📊 开始处理CSV文件: {csv_path}")
        # 先尝试utf-8，再尝试gbk
        try:
            df = pd.read_csv(csv_path, encoding='utf-8')
        except UnicodeDecodeError:
            print("⚠️ UTF-8解码失败，尝试GBK编码重新读取")
            df = pd.read_csv(csv_path, encoding='gbk')
        df = df.dropna(how='all')
        df.columns = [str(col) for col in df.columns]
        if '日期' in df.columns:
            df['日期'] = pd.to_datetime(df['日期']).dt.strftime('%Y-%m-%d')
        records = df.to_dict(orient='records')
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(records, f, ensure_ascii=False, indent=2)
        print(f"✅ 成功转换 {len(records)} 条记录到 {json_path}")
        if records:
            print(f"📅 最新记录: {records[-1]['日期']} - {records[-1]['体重']}kg")
        return True
    except Exception as e:
        print(f"❌ 处理失败: {str(e)}")
        return False

if __name__ == "__main__":
    success = csv_to_json("weight.csv", "weight.json")
    if not success:
        exit(1)