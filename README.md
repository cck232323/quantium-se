# 🛍️ Pink Morsel Sales Dashboard (Quantium-style Project)

This project is a full-stack data analysis dashboard built with [Plotly Dash](https://dash.plotly.com/), designed to analyze and visualize sales performance for a specific product (`pink morsel`) across multiple CSV datasets. Inspired by Quantium's data science challenges, the project focuses on:

- 🧹 Cleaning real-world CSV inputs
- 📊 Generating sales summary outputs
- 📈 Visualizing time-based trends
- 🧩 Modular and testable backend logic

---

## 🚀 Features

- **File Loader**: Recursively loads all `.csv` sales files from a `/data` folder
- **Data Cleaner**: Cleans price formats (e.g., `$4.99`) and filters for `"pink morsel"` entries
- **Sales Calculator**: Computes `sales = price * quantity` per record and outputs `output.csv`
- **Dashboard UI**: Interactive Dash interface with Bootstrap layout and buttons
- **Visualization**: Dynamic line chart showing sales over time
- **Engineering Best Practices**: Modular structure, testable utils, clean callback separation

---

## 📂 Project Structure
quantium-sofrware-engineering/
├── run.py               # Entry point
├── requirements.txt     # Python dependencies
├── dash_app/
│   ├── app.py           # App init
│   ├── layout.py        # UI layout
│   ├── callbacks/       # Interaction logic (buttons → computation)
│   └── utils/           # Data processing logic
├── tests/               # Pytest-based unit tests
├── data/                # Place input CSVs here
├── output/              # Output generated CSV will be saved here
└── README.md

---

## 🛠️ How to Run

```bash
# Setup
pip install -r requirements.txt

# Run
python run.py

# Then open http://127.0.0.1:8050 in your browser

