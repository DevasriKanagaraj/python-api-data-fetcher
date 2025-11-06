import requests
import sqlite3
import json
from datetime import datetime

DB = "api_data.db"

def setup_db():
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS api_results(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            source TEXT,
            payload TEXT,
            fetched_at TEXT
        )
    """)
    conn.commit()
    conn.close()


def fetch_api_data(url):
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()


def store_data(source, data):
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO api_results (source, payload, fetched_at)
        VALUES (?, ?, ?)
    """, (source, json.dumps(data), str(datetime.now())))
    conn.commit()
    conn.close()


def fetch_and_store(url):
    print(f"Fetching from {url}")
    data = fetch_api_data(url)
    store_data(url, data)
    print("✅ Data stored successfully.\n")


if __name__ == "__main__":
    setup_db()

    # Example public API (replace with any API you want)
    API_URL = "https://api.github.com/repos/python/cpython"

    fetch_and_store(API_URL)
