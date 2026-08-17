# AI-SQL Dashboard

An AI-powered SQL dashboard that allows users to interact with data using natural-language queries and generate SQL-based insights and visualizations.

## Features

* Natural-language to SQL query generation
* AI-assisted SQL analysis
* Database connectivity
* Retail sales dataset for analysis
* Data visualization and metrics
* SQL agent workflow
* Connection and agent tests

## Project Structure

```text
AI-SQL-Dashboard/
│
├── agent/
│   ├── llm.py
│   ├── prompts.py
│   └── sql_agent.py
│
├── dashboard/
│   ├── charts.py
│   └── metrics.py
│
├── database/
│   ├── create_db.py
│   ├── db_connection.py
│   ├── load_data.py
│   └── schema.sql
│
├── datasets/
│   └── retail_sales.csv
│
├── tests/
│   ├── test_connection.py
│   ├── test_llm.py
│   └── test_sql_agent.py
│
├── app.py
├── main.py
├── requirements.txt
└── README.md
```

## Technologies

* Python
* SQL
* Large Language Models (LLMs)
* Database Management
* Data Visualization
* AI/ML

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/rishi-1103/AI-SQL-Dashboard.git
cd AI-SQL-Dashboard
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root and add the required API/database credentials.

**Do not commit the `.env` file to GitHub.**

### 5. Run the application

```bash
python app.py
```

## Dataset

The project includes a sample retail sales dataset for demonstrating SQL queries, analytics, metrics, and visualizations.

## Testing

Run the tests with:

```bash
pytest
```

## Author

**Rishi Barman**

GitHub: https://github.com/rishi-1103
