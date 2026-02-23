# 📊 Dataset Analysis Project

A Python-based data analysis project that reads a student performance dataset, performs statistical analysis, and automatically generates a detailed text report.

---

## 🎯 Objective

To analyze student academic performance using Python and Pandas, and generate an automatic analysis report covering totals, averages, top performers, and department-wise insights.

---

## 📁 Project Structure

```
dataset-analysis-project/
│
├── data/
│   └── students_performance.csv   # Student dataset (15 records)
│
├── src/
│   └── dataset_analysis.py        # Main analysis script
│
├── output/
│   └── analysis_report.txt        # Auto-generated output report
│
├── requirements.txt               # Python dependencies
└── README.md                      # Project documentation
```

---

## 🛠️ Technologies Used

| Tool       | Purpose                        |
|------------|--------------------------------|
| Python 3.x | Core programming language      |
| Pandas     | Data loading and analysis      |
| OS Module  | File path and directory handling |
| Datetime   | Timestamp for the report       |

---

## 📋 Features

- ✅ Loads student dataset from CSV using Pandas
- ✅ Calculates total marks and average for each student
- ✅ Assigns grades automatically (A+, A, B, C, D)
- ✅ Identifies the top-performing student
- ✅ Performs department-wise analysis
- ✅ Generates a complete text report automatically

---

## 🚀 How to Run

### 1. Clone the repository
```bash
git clone https://github.com/your-username/dataset-analysis-project.git
cd dataset-analysis-project
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the analysis script
```bash
python src/dataset_analysis.py
```

### 4. View the report
```
output/analysis_report.txt
```

---

## 📊 Dataset Overview

The dataset (`students_performance.csv`) contains 15 student records with the following columns:

| Column     | Description              |
|------------|--------------------------|
| StudentID  | Unique student ID        |
| Name       | Student name             |
| Department | Academic department      |
| Math       | Math marks (out of 100)  |
| Science    | Science marks            |
| English    | English marks            |
| History    | History marks            |
| Computer   | Computer marks           |

**Departments covered:** Computer Science, Electronics, Mechanical

---

## 📄 Sample Report Output

```
============================================================
       STUDENT PERFORMANCE ANALYSIS REPORT
============================================================
Generated on : 2024-01-15 10:30:00
Total Records: 15

OVERALL STATISTICS
------------------------------------------------------------
Highest Average Score : 95.4
Class Average Score   : 78.6

TOP PERFORMING STUDENT
------------------------------------------------------------
  Name       : Meera Joshi
  Department : Computer Science
  Total Marks: 463
  Grade      : A+
...
```

---

## 👨‍💻 Division of Work

| Task                        | Owner  |
|-----------------------------|--------|
| Dataset creation            | You    |
| Pandas analysis logic       | You    |
| Report generation           | You    |
| Visualization               | Partner|
| README documentation        | Partner|
| GitHub setup & structure    | Partner|

---

## 📌 Internship Project

This project was developed as part of the internship evaluation to demonstrate practical Python data analysis skills.
