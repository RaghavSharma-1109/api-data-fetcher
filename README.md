# 🪙 Crypto CLI Tracker

A modular, pipeline-based Python CLI tool that fetches live cryptocurrency prices from the CoinGecko API, validates and processes the data, and stores it in a structured text file with timestamps.

---

## 📌 Features

- 🔗 Fetch real-time crypto prices via CoinGecko public API
- ✅ Validate API responses before processing (missing coins, currencies, null values)
- 🧹 Clean and structure raw API data
- ⚙️ Process data into storage-ready records with timestamps
- 💾 Append results to a formatted `.txt` report file
- 📋 Full logging to `app.log` (DEBUG level) and console (WARNING level)
- ❌ Consistent error handling at every stage of the pipeline

---

## 🏗️ Project Structure

```
api-data-fetcher/
│
├── api/
│   └── fetcher.py          # API call logic (CoinGecko)
│
├── Validator/
│   └── validator.py        # Validates raw API response
│
├── datacleaner/
│   └── data_cleaner.py     # Cleans and structures validated data
│
├── processor/
│   └── data_processor.py   # Converts data into storage-ready records
│
├── report_handler.py       # Handles file storage and formatting
├── config.py               # Centralized config (URL, timeout, filepath)
├── main.py                 # Entry point and pipeline controller
├── requirements.txt        # Project dependencies
└── README.md
```

---

## ⚙️ Pipeline

```
User Input
    ↓
Fetcher (CoinGecko API Call)
    ↓
Validator (Response Integrity Check)
    ↓
Data Cleaner (Structure & Normalize)
    ↓
Data Processor (Add Timestamps)
    ↓
Report Handler (Append to .txt File)
```

Each stage uses a consistent return contract:
```python
{
    "success": True/False,
    "data": <payload or None>,
    "error": <error message or None>
}
```

---

## 🧠 Tech Stack

- Python 3
- `requests` — HTTP calls to CoinGecko API
- `logging` — Dual-handler logging (file + console)
- `datetime` — Timestamping records
- `os` — File path management

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/RaghavSharma-1109/api-data-fetcher.git
cd api-data-fetcher
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the project

```bash
python main.py
```

---

## 💡 Example Usage

```
Enter cryptocoins: bitcoin, ethereum
Enter exchange currency: usd, inr
```

---

## 📄 Sample Output (`crypto_data.txt`)

```
Coin           |Currency|Price        |Timestamp      
---------------|--------|-------------|---------------
bitcoin        |usd     |67000        |2026-06-12 18:00:28
bitcoin        |inr     |5600000      |2026-06-12 18:00:28
ethereum       |usd     |3500         |2026-06-12 18:00:28
ethereum       |inr     |290000       |2026-06-12 18:00:28
```

---

## ⚠️ Error Handling

The pipeline handles errors at every stage:

| Stage | Errors Handled |
|---|---|
| Fetcher | Timeout, ConnectionError, HTTPError |
| Validator | None response, missing coins, missing currencies, wrong types |
| Data Cleaner | Invalid input types, missing keys |
| Data Processor | Empty dataset |
| Report Handler | No records to write |

All errors are logged to `app.log` with timestamps and severity levels.

---

## 📋 Logging

- `app.log` — Full DEBUG-level log of every pipeline stage
- Console — WARNING and above only (errors visible without noise)

Log format: `%(asctime)s - %(levelname)s - %(message)s`

---

## 🚀 Future Improvements

- [ ] Export to CSV / JSON format
- [ ] SQLite database storage (replacing `.txt`)
- [ ] Flask REST API wrapper
- [ ] Scheduled auto-fetch (cron / APScheduler)
- [ ] Historical data viewer
- [ ] Docker deployment

---

## 🧠 Learning Outcomes

- Modular backend pipeline design
- API integration with error handling
- Input validation layer architecture
- Structured logging with dual handlers
- Professional Python project structure

---

## 👨‍💻 Author

**Raghav Sharma**
[GitHub — RaghavSharma-1109](https://github.com/RaghavSharma-1109)