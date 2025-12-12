import requests    
import json        
import sqlite3     
from datetime import datetime 
import pandas as pd 

API_KEY = "aef5b771bd07a930d7fc3343c142077f" 
CITY = "Sumgait" 
DB_NAME = "weather_data.db" 
TABLE_NAME = "weather_records" 


def extract_weather_data(api_key, city):
    URL = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    print(f"1. EXTRACT: Data request for {city}")
    
    try:
        response = requests.get(URL)
        response.raise_for_status() 
        raw_data = response.json()
        print("Data are successfuly extracted in form of JSON.")   
        return raw_data
        
    except requests.exceptions.RequestException as e:
        print(f"ERROR EXTRACT: Problem with a request or internet: {e}")
        return None
    
    
def transform_weather_data(raw_data):
    if not raw_data:
        return None

    print("2. TRANSFORM: Data Conversion")
    
    try:
        main_info = raw_data.get('main', {}) 
        weather_info = raw_data.get('weather', [{}])[0] 
        
        city_name = raw_data.get('name')
        temp = main_info.get('temp')
        humidity = main_info.get('humidity')
        description = weather_info.get('description')
        
        timestamp = raw_data.get('dt')
        date_time = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

        data = {
            'collection_time': [date_time],
            'city': [city_name],
            'temperature_c': [temp],
            'humidity_percent': [humidity],
            'description': [description]
        }
        
        df = pd.DataFrame(data)
        print("The data has been successfully converted to a DataFrame.")
        return df
    
    except Exception as e:
        print(f"ERROR TRANSFORM: Parsing or formatting problem: {e}")
        return None
    
def load_data_to_sqlite(df, db_name, table_name):
    
    if df is None or df.empty:
        print("No data available for download.")
        return

    print(f"3. LOAD: Loading into the database {db_name}")
    
    try:
        conn = sqlite3.connect(db_name)
        
        df.to_sql(table_name, conn, if_exists='append', index=False)
        
        print(f"Successfully loaded {len(df)} rows into the table '{table_name}'.")
        
        test_df = pd.read_sql_query(f"SELECT * FROM {table_name} ORDER BY collection_time DESC LIMIT 1", conn)
        print("Download check (last entry):")
        print(test_df)
        
        conn.close()
        
    except Exception as e:
        print(f"ERROR LOAD: Problem with writing to SQLite: {e}")
        
        

def run_weather_etl():
    print("  START OF ETL PIPELINE FOR WEATHER DATA  ")
    
    # Extract
    raw_data = extract_weather_data(API_KEY, CITY)
    
    if raw_data:
        # Transform
        cleaned_df = transform_weather_data(raw_data)
        
        if cleaned_df is not None:
            # Load
            load_data_to_sqlite(cleaned_df, DB_NAME, TABLE_NAME)
    
    print("     ETL PIPELINE COMPLETED        ")

if __name__ == "__main__":
    run_weather_etl()