# 📊 Crypto Price Tracker

A simple and powerful web app that tracks real-time cryptocurrency prices using CoinGecko API, MySQL database, and a beautiful chart powered by **Matplotlib** and **Streamlit**.

---

## 🚀 Features

- 📈 Interactive graph with 5-point moving average
- 💹 Hover tooltips to explore individual price points
- 🕒 Historical data stored every minute
- 🧠 Smart decimal formatting based on price scale
- 🔒 Secure `.env` file to manage API keys and database credentials

---

## 📦 Tech Stack

- Python 3
- MySQL
- Streamlit
- Matplotlib
- CoinGecko API
- dotenv

---

## 🔧 Installation

1. **Clone the repo**

   git clone https://github.com/your-username/crypto-tracker.git
   cd crypto-tracker

2. **Create a virtual environment (optional but recommended)**
    python -m venv venv
    source venv/bin/activate  # or venv\Scripts\activate on Windows

3. **Install dependencies**
    pip install -r requirements.txt


📁 Project Structure
bash
Copy
Edit
crypto-tracker/
├── app.py           # Streamlit frontend for chart
├── data.py          # Script to fetch and store data from CoinGecko
├── db_config.py     # DB connection setup
├── .env             # Your environment variables (not tracked in Git)
├── requirements.txt # Python dependencies
🗝️ .env Example
Create a .env file with the following:

ini
Copy
Edit
DB_HOST=localhost
DB_USER=your_mysql_username
DB_PASS=your_mysql_password
DB_NAME=your_database_name
API_KEY=your_coingecko_api_key
🔐 Be sure to add .env to .gitignore to avoid pushing secrets to GitHub.

🛠️ Run Locally
1. Start the data fetcher (in background)
bash
Copy
Edit
python data.py
This script fetches price data for the top 150 coins every minute and saves it in your MySQL database.

2. Run the web app
bash
Copy
Edit
streamlit run app.py
Visit http://localhost:8501 in your browser.

🌐 Deployment Guide
You can host this project using:

Streamlit Community Cloud (recommended for quick deploys)

Render / Railway (for more control)

PlanetScale or Railway for free managed MySQL

A full deployment tutorial is available here (Coming soon...)

🙌 Acknowledgements
CoinGecko API

Streamlit

Matplotlib

PlanetScale

Railway

