from sqlalchemy import create_engine
import pandas as pd

HOST = "localhost"
PORT = 3306
DATABASE = 'pytest1'
DRIVER = "ODBC+17+for+SQL+Server"
USERNAME = 'root'
PASSWORD = ''

SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
sql_engine = create_engine(SQLALCHEMY_DATABASE_URL)

df = pd.read_sql("SELECT email FROM users", con=sql_engine)
print(df)   