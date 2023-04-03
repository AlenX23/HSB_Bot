import os.path
import pandas as pd
import sqlite3


def export():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, "reviews.db")

    conn = sqlite3.connect(db_path)
    df = pd.read_sql('select * from questionnaire', conn)
    df.to_excel('result.xlsx', index=False)
