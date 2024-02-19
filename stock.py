import pandas as pd
import pymysql
from datetime import datetime
from dotenv import load_dotenv
import os


# Load environment variables from .env file
load_dotenv()

# Get environment variables
host = os.getenv("host")
username = os.getenv("user_name")
password = os.getenv("password")
database = os.getenv("database")

# Connect to MySQL database
db_connection = pymysql.connect(
    host=host,
    user=username,
    password=password,
    database=database
)




# Create a cursor
cursor = db_connection.cursor()

def stock_data():
    # Read data from Excel sheet
    df = pd.read_csv(r'C:\Users\DELL\Desktop\Information retrieval\data\retail_2009.csv', encoding='cp1252')


    df.fillna('', inplace=True)
    # Define the SQL INSERT statement
    insert_query = """
        INSERT INTO retail_data (
            Invoice, StockCode, Description, Quantity, InvoiceDate, Price, CustomerID, Country
        ) VALUES (
            %s, %s, %s, %s, %s, %s, %s, %s
        )
    """


    # Insert data into the database
    for index, row in df.iterrows():
        data = (
            row['Invoice'], row['StockCode'], row['Description'], row['Quantity'],
            datetime.strptime(row['InvoiceDate'], '%m/%d/%Y %H:%M'), row['Price'], row['Customer ID'], row['Country']
        )

        try:
            # print(insert_query%(data))
            print('inserting ---', index)
            cursor.execute(insert_query, data)
            
        except pymysql.err.DataError:
            continue
        
stock_data()
# Commit changes and close the connection
db_connection.commit()
db_connection.close()        