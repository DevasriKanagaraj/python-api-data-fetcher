# python-api-data-fetcher

A lightweight data-ingestion utility that fetches JSON from any public API and stores the results in a local SQLite database. Ideal for rapid prototyping, analytics pipelines, automation scripts, and API exploration.

---

## 🚀 Features

- Fetches JSON from any API endpoint  
- Automatically creates a local SQLite database  
- Stores API responses with timestamps  
- Simple, clean, extensible Python code  
- Works on Windows, macOS, and Linux  

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/DevasriKanagaraj/python-api-data-fetcher.git
cd python-api-data-fetcher
```

Create and activate a virtual environment:

### Windows:
```bash
python -m venv .venv
.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the script:

```bash
python fetcher.py
```

Expected output:

```
Fetching from https://api.github.com/repos/python/cpython
✅ Data stored successfully.
```

---

## 🗄 Where is the data stored?

The script creates a SQLite database file named:

```
api_data.db
```

To view the stored content:

```python
import sqlite3

conn = sqlite3.connect("api_data.db")
cur = conn.cursor()
cur.execute("SELECT * FROM api_results")
print(cur.fetchall())
```

---

## 🛠 Customizing the API URL

Edit this line in `fetcher.py`:

```python
API_URL = "https://api.github.com/repos/python/cpython"
```

Replace it with any API URL you want to fetch from.

---

## 🧩 Project Structure

```
python-api-data-fetcher/
│
├── fetcher.py         # Main script
├── api_data.db        # Created after running the script
├── requirements.txt   # Dependencies
├── README.md          # Project documentation
└── .venv/             # Virtual environment (ignored in Git)
```

---

## 🧭 Future Enhancements

- CLI support (`python fetcher.py --url <API>`)
- Scheduled ingestion
- Docker version
- Dashboard for viewing data

---

## 📄 License

MIT License
