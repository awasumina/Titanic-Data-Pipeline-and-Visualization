import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
load_dotenv()
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
host = os.getenv("HOST")
port = os.getenv("PORT")
dbname = os.getenv("DBNAME")

def load_to_postgres():

    engine = create_engine(f"postgresql://{username}:{password}@{host}:{port}/{dbname}")
    print(engine)

    # base_path = "../data"
    # print(f"Loading data from base path: {base_path}")

    # if not os.path.exists(base_path):
    #     print("data folder not found.")
    #     return

    # for category in os.listdir(base_path):
    #     category_path = os.path.join(base_path, category)
    #     print(f"Processing category: {category}")
    #     # if not os.path.isdir(category_path):
    #     #     continue

    #     print(f"Loading data for category: {category}")

    #     dim_path = os.path.join(category_path)
    #     print(f"Dimension path: {dim_path}")
    #     if os.path.exists(dim_path):
    #         try:
    #             df = pd.read_csv(dim_path)
    #             df.to_sql(f"{category}_rawTitanic", engine, if_exists="append", index=False)
    #             print(f"Loaded: {dim_path}")
    #         except Exception as e:
    #             print(f"Error loading {dim_path}: {e}")

       
load_to_postgres()
