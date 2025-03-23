import requests
import pandas as pd
import sqlite3

def main():
    # Fetch data
    API_URL = "https://restcountries.com/v3.1/all"
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        data = response.json()
        print("Data fetched successfully")
    except requests.RequestException as e:
        print(f"Failed to fetch data: {e}")
        return

    # Transform data
    countries = [
        {
            'name': country.get('name', {}).get('common', 'Unknown'),
            'capital': country.get('capital', [None])[0],
            'population': country.get('population', 0)
        }
        for country in data
    ]
    df = pd.DataFrame(countries)
    print("Data transformed successfully")

    # Load data into SQLite
    try:
        conn = sqlite3.connect('countries.db')
        conn.execute('''
        CREATE TABLE IF NOT EXISTS countries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            capital TEXT,
            population INTEGER,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        ''')
        df.to_sql('countries', conn, if_exists='append', index=False)
        conn.commit()
        print("Data loaded successfully")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    main()