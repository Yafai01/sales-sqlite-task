# Sales Summary Analysis using SQLite and Python

**Author:** Yafai  
**Role:** Data Analyst Intern Candidate  

---

## 📌 Project Overview
This project demonstrates how to use **SQL inside Python** to extract basic sales insights from a **SQLite database** and visualize the results using a simple bar chart.  
The task focuses on writing SQL queries, integrating them with Python, and presenting summarized sales data clearly.

---

## 🎯 Objective
- Connect Python to a SQLite database  
- Run SQL queries to calculate:
  - Total quantity sold per product  
  - Total revenue per product  
- Display results using print statements  
- Visualize revenue using a basic bar chart  

---

## 🛠 Tools & Technologies
- **Python**
- **SQLite** (via `sqlite3`)
- **pandas**
- **matplotlib**
- **VS Code**

---

## 📂 Project Structure
sales-sqlite-task/
│
├── sales_analysis.py # Main Python script
├── sales_data.db # SQLite database file
├── sales_chart.png # Revenue bar chart output
└── README.md # Project documentation

yaml
Copy code

---

## 🧠 What This Project Does
1. Creates a SQLite database with a `sales` table  
2. Inserts sample sales data  
3. Executes SQL queries using `GROUP BY` to summarize sales  
4. Loads SQL results into pandas DataFrame  
5. Prints sales summary  
6. Generates and saves a revenue bar chart  

---

## 📊 Output
- Console output showing total quantity and revenue per product  
- Bar chart visualization of revenue (`sales_chart.png`)  

---

## ▶️ How to Run the Project
1. Clone the repository:
```bash
git clone https://github.com/Yafai01/sales-sqlite-task.git
Navigate to the project folder:

bash
Copy code
cd sales-sqlite-task
Install required libraries:

bash
Copy code
pip install pandas matplotlib
Run the script:

bash
Copy code
python sales_analysis.py
📚 Key Concepts Demonstrated
SQL queries inside Python

GROUP BY and aggregate functions

Database-to-DataFrame workflow

Basic data visualization

✅ Outcome
By completing this project, I gained hands-on experience in:

Writing and executing SQL queries

Integrating databases with Python

Performing basic data analysis

Visualizing business data clearly

📎 Notes
This project was completed as part of a Data Analyst Internship Task to demonstrate foundational data analysis skills using SQL and Python.
