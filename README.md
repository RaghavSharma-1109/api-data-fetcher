# 🚀 Crypto CLI Tracker

A command-line based Python tool that fetches live cryptocurrency prices, processes the data, and stores it in a structured format.

---

## 📌 Features

- 🔗 Fetch real-time crypto prices using CoinGecko API
- 🧹 Clean and validate API data
- ⚙️ Process data into structured records
- 💾 Store results in a formatted text file
- 📊 CLI-based user interaction
- ❌ Error handling at every stage

---

## 🏗️ Project Structure
api-data-fetcher/
│
├── api/
│ └── fetcher.py # API call logic
│
├── datacleaner/
│ └── data_cleaner.py # Cleans and structures raw data
│
├── processor/
│ └── data_processor.py # Converts data into storage-ready format
│
├── report_handler.py # Handles file storage
├── main.py # Entry point (controller)
├── crypto_data.txt # Output file
└── README.md

---

## ⚙️ How It Works
User Input
↓
Fetcher (API Call)
↓
Data Cleaner
↓
Data Processor
↓
Report Handler (File Storage)

---

## 🧠 Tech Stack

- Python 3
- Requests Library
- CoinGecko API

---

## ▶️ How to Run

### 1. Clone the repository
git clone https://github.com/RaghavSharma-1109/api-data-fetcher
cd api-data-fetcher

### 2. Install dependencies
pip install requests


### 3. Run the project


python main.py


---

## 💡 Example Usage
Enter cryptocoins: bitcoin, ethereum, tether
Enter exchange currency: usd, inr

---

## 📄 Sample Output

Coin | Currency | Price | Timestamp

bitcoin | usd | 67000 | 2026-05-27 19:03:39
ethereum | inr | 197456 | 2026-05-27 19:03:39
---

## ⚠️ Error Handling

- Invalid user input
- API failures (timeout, connection error)
- Missing coins or currencies
- Empty dataset

---

## 🚀 Future Improvements

- Add CSV/JSON export
- Add data filtering (by coin/currency)
- Add history viewer
- Add GUI (Tkinter/Web)
- Replace file storage with database (SQLite)

---

## 🧠 Learning Outcomes

- Modular backend design
- Data processing pipelines
- API integration
- Error handling strategies
- CLI-based application development

---

## 📌 Note

This project is designed as a learning-focused backend system and can be extended into a full-fledged application.

---

## 👨‍💻 Author

Raghav Sharma
